models.py

from django.db import models
# from django.template.defaultfilters import slugify
from helper import slugify



class Type(models.Model):
    name=models.CharField(max_length=250)
    stages=models.ManyToManyField('Stage', through="StagesByType", null=True, blank=True)
    parts=models.ManyToManyField('self', through='PartsByType', symmetrical=False, null=True, blank=True )
    # parts=models.ManyToManyField('self', symmetrical=False)
    
    class Meta:
        verbose_name="Тип"
        verbose_name_plural="Типы"


    def __str__(self) -> str:
        return f'{self.name}'
    

class Stage(models.Model):
    
    name=models.CharField(max_length=250)
    number=models.IntegerField(unique=True)

    class Meta:
        ordering=['number']
        verbose_name="Этап"
        verbose_name_plural="Этапы"
        

    def __str__(self) -> str:
        return f'{self.name}-{self.number}'
    

class StagesByType(models.Model):
    type=models.ForeignKey('Type', related_name="type_set_by_stage", on_delete=models.CASCADE)
    stage=models.ForeignKey('Stage', related_name="stage_set", on_delete=models.CASCADE)


class PartsByType(models.Model):
    type=models.ForeignKey('Type', related_name="type_set", on_delete=models.CASCADE),
    part=models.ForeignKey('Type', related_name="part_set",  on_delete=models.CASCADE),
    kol_vo=models.IntegerField()

    

forms.py

from django import forms
from .models import Stage, Type, PartsByType, StagesByType


# class AddCategoryForm(forms.ModelForm):

#     class Meta:
#         model=Category
#         fields=["name", "parent"]
#         widgets={
#             "name":forms.TextInput(),
#             "parent":forms.Select(choices=Category.objects.all().values_list())
#         }

#  class AddPartsForm(forms.ModelForm):

#     class Meta:
#         model=Category
#         fields=["name", "parent"]
#         widgets={
#             "name":forms.TextInput(),
#             "parent":forms.Select(choices=Category.objects.all().values_list())
#         }
class AddStageForm(forms.ModelForm):
    '''Форма добавления этапа'''

    class Meta:
        model= Stage
        fields=["name", "number"]
        widgets={
            "name":forms.TextInput(attrs={"class":"formfield formfield__inputtext"}),
            "number":forms.NumberInput(attrs={"class":"formfield formfield__inputnumber"}) 
        }
        labels={
            "name": "Название этапа",
            "number": "Номер этапа"
        }


class AddTypeForm(forms.ModelForm):
    '''Форма добавления типа продукта'''
    # parts=forms.ModelMultipleChoiceField(PartByType.objects.all(),widget=forms.CheckboxSelectMultiple(attrs={"class":"formfield formfield__checkbox"}), required=False)
    # stages= forms.ModelMultipleChoiceField(Stage.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={"class":"formfield formfield__checkbox"}))

    class Meta:
        model=Type
        fields=['name']
        widgets={
            "name": forms.TextInput(attrs={"class":"formfield formfield__inputtext"}),
           
        }


class AddStageByTypeForm(forms.ModelForm):
    '''Форма добавления этапа производства для типа'''
    type=forms.ModelChoiceField(Type.objects.all(), widget=forms.HiddenInput())
    stage=forms.ModelChoiceField(Stage.objects.all(), widget=forms.Select(attrs={"class":"formfield formfield__select"}) )

    class Meta:
        model=StagesByType
        fields=['type', 'stage']


class AddPartByTypeForm(forms.ModelForm):
    '''Форма добавления комплектующего для типа'''
    type=forms.CharField(widget=forms.HiddenInput())
    part=forms.ModelChoiceField(Type.objects.all(), label="Тип комплектующего" , widget=forms.Select(attrs={"class":"formfield formfield__select"}))
    
    class Meta:
        model=PartsByType
        fields=["type", "part", "kol_vo"]
        widget={
            "kol_vo":forms.NumberInput(attrs={"class":"formfield formfield__inputnumber"})
        }




views.py

from typing import Any
from django.shortcuts import render, redirect
from django.http import Http404
from django.views import View
from .utils import MainPageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddTypeForm, AddStageForm, AddStageByTypeForm, AddPartByTypeForm
from .models import Stage, Type


# Create your views here.


class MainPage( LoginRequiredMixin, MainPageMixin, View):
    '''Главная страница передадим  "Главное  меню"'''
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context=super().get_context_data()
        return context
    

    def get(self,req, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная страница"
        return render(req,'search/index.html', context)


class AddStage(LoginRequiredMixin, MainPageMixin, View):
    '''Добавление этапа'''
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context['title']='Добавление этапа'
        return context
    
    def get(self, req, *args, **kwargs):
        context=self.get_context_data()
        form=AddStageForm()
        context['form']=form
        return render(req, 'search/index.html', context)
    
    def post(self, req, *args, **kwargs):
        context=self.get_context_data()
        form=AddStageForm(req.POST)
        if form.is_valid():
            cd=form.cleaned_data
            try:
                new_stage=Stage(**cd)
                new_stage.save()
                form=AddStageForm()
            except:
                form.add_error(None, "Ошибка при добавлении в базу")
        context['form']=form
        return render(req, 'search/index.html', context)
        
        
class AddType(LoginRequiredMixin, MainPageMixin, View):

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context['title']="Добавление типа"
        return context
    
    def get(self, req, *args, **kwargs):
        context=self.get_context_data()
        form=AddTypeForm()
        templated_form=form.render('search/forms/all_in_column.html')
        context['form']=templated_form
        # form.stages=Stage.objects.filter(pk=1)
        # form.fields['stages'].queryset=Stage.objects.filter(pk=1) 
        return render(req,'search/add_type.html', context )

    def post(self, req, *args, **kwargs):
        context=self.get_context_data()
        form=AddTypeForm(req.POST)
        if form.is_valid():
            cd=form.cleaned_data
            try:
                new_type= Type(**cd)
                new_type.save()
                form=AddTypeForm()
            except:
                # print('ffffffff')
                form.add_error(None, "Ошибка при добавлении в базу")
        context['form']=form.render('search/forms/all_in_column.html')
        return render(req,'search/add_type.html', context )


class ListType(LoginRequiredMixin, MainPageMixin, View):
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context['title']="Типы продукции"
        list_types=Type.objects.all()
        context['list_types']=list_types
        return context
    

    def get(self, req, *args, **kwargs):
        context=self.get_context_data()
        return render(req, 'search/list_type.html', context)
        


class EditType(LoginRequiredMixin, MainPageMixin, View):
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context['title']="Редактирование типа"
        return context
    

    def get(self, req, *args, **kwargs):
        context=self.get_context_data()
        type_id=kwargs.get('type_id')
        context['type_id']=type_id
        # add_part_by_type_form.fields['type'].queryset=type_id
        context['add_stage_by_type_form']=AddStageByTypeForm(initial={'type':type_id})
        context['add_part_by_type_form']=AddPartByTypeForm(initial={'type':type_id})
        return render(req, 'search/edit_type.html', context)




class DelType(LoginRequiredMixin, MainPageMixin, View):
     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context['title']="Типы продукции"
        list_types=Type.objects.all()
        context['list_types']=list_types
        return context
     

     def get(self, req, *args, **kwargs):
        type_id=kwargs.get('type_id')
        try:
            Type.objects.get(pk=type_id).delete()
            return redirect('list_type')
        except:
            raise Http404() 

urls.py

"""
URL configuration for loginov project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from user import urls as user_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainPage.as_view(), name="main"),
    path('user/', include(user_urls, namespace="user")),
    # Этапы ######################################################################### 
    path('stage/add/', views.AddStage.as_view(), name="add_stage"),
    # Типы #########################################################################
    path('type/add/', views.AddType.as_view(), name="add_type"),
    path('type/list/', views.ListType.as_view(), name="list_type"),
    path('type/<int:type_id>/edit/', views.EditType.as_view(), name="edit_type"),
    path('type/<int:type_id>/del/', views.DelType.as_view(), name="del_type"),
    
]

///////////////////////////////////////////////////////////////////////////////////////////////////

class EditType(LoginRequiredMixin, MainPageMixin, View):
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context['title']="Редактирование типа"
        return context
    
    def get_queryset_available_stages(self, type_id):
        list_queryset_all_stages= list(Stage.objects.all())
        list_queryset_exists_stages=list(Type.objects.get(pk=type_id).stages.all())
        '''вычисляем list id-ишников оставшихся этапов'''
        list_id_new_stages=[x.id for x in list_queryset_all_stages if x not in list_queryset_exists_stages]
        queryset_available_stages=Stage.objects.filter(pk__in=list_id_new_stages)
        return queryset_available_stages
        



    def get(self, req, *args, **kwargs):
        context=self.get_context_data(**kwargs)
        type_id=kwargs.get('type_id')
        type=Type.objects.get(pk=type_id)
        context['type_id']=type_id
        add_stage_by_type_form=AddStageByTypeForm(initial={'type':type_id})
        add_stage_by_type_form.fields['stage'].queryset=self.get_queryset_available_stages(type_id)
       
        print(list(type.stages.all()))
       
        # add_stage_by_type_form.fields['stage'].queryset=Stage.objects.exclude(id__in=type.stages)
        context['add_stage_by_type_form']=add_stage_by_type_form
        context['add_part_by_type_form']=AddPartByTypeForm(initial={'type':type_id})
        return render(req, 'search/edit_type.html', context)

////////////////////////////////////////////////////////////////////////////////
