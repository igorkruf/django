from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.conf import settings 
from django.views import View

from typing import List
from django.views.generic import TemplateView, CreateView, FormView
from .forms import  AddTypeForm, AddSetTypeForm, AddProductForm
from .models import  Type, SetType, Product

class GetListTypes(LoginRequiredMixin, View):
    
    def get(self, req, *args, **kwargs):
        pass

class AddSetType(LoginRequiredMixin, View):
    login_url='user:login'
    

    def get(self, req, *args, **kwargs):
        data=kwargs
        data['title']='Добавляем комплектующие'
        type=Type.objects.get(pk=data['type_id'])
        data['form']=AddSetTypeForm()
        data['type']=type
        list_types_for_part=self.get_types_for_set(data['type_id'])
        data['list_types_for_part']=list_types_for_part
        ddd=SetType.objects.filter(type_id=data['type_id'])
        print(ddd)
        data['list_parts_for_type']=self.get_list_parts(data['type_id'])
        print(data['list_parts_for_type'])
        return render(req,'product/add_set_type.html', data)
    

    def post(self, req, *args, **kwargs):
        form=AddSetTypeForm(req.POST)
        data=kwargs
        data['title']='Добавляем комплектующие'
        type=Type.objects.get(pk=data['type_id'])
        data['type']=type
        list_types_for_part=self.get_types_for_set(data['type_id'])
        data['list_types_for_part']=list_types_for_part
        data['list_parts_for_type']=self.get_list_parts(data['type_id'])
        if form.is_valid():
            print('Всё верно')
            cd=form.cleaned_data
            try:
                SetType.objects.create(**cd)
                form=AddSetTypeForm()
                
            except:
                form.add_error(None, "Ошибка при добавлении записи в базу")
        data['form']=form        
        return render(req,'product/add_set_type.html', data)
   

    def get_types_for_set(self ,type_id):

        list_exclude=[]
        
        collection_types=Type.objects.all().exclude(pk=type_id)
        list_dict_collection_types=collection_types.values("id", "name")
        print(list_dict_collection_types)
        for dict_collection_types in list_dict_collection_types:
            set_by_type=SetType.objects.filter(type=dict_collection_types['id']).values("type_id","part_id")
            print(set_by_type)
            for dict_collection_parts in set_by_type:
                if  dict_collection_parts['part_id']==type_id:
                    list_exclude.append(dict_collection_parts['type'])
        collection_types_final=collection_types.exclude(pk__in=list_exclude)
        return collection_types_final
    


    def get_list_parts(self, type_id):

        return SetType.objects.filter(type_id=type_id)


    

class AddProduct(View):

    def get(self, req, *args, **kwargs):
        form=AddProductForm()
        return render(req, "product/add_product.html", {"form":form}) 

    def post(self, req, *args, **kwargs):
        
        
        form=AddProductForm(req.POST)
        # print(f'ddddddddddddd: {form.user}')
        data=kwargs
        if form.is_valid():
            print('Всё верно')
            cd=form.cleaned_data
                        
            try:
                #Product.objects.create(**cd)
                product=Product(**cd)
                #new_product.save(commit=False)
                product.save()
                form=AddProductForm()
                
            except:
                form.add_error(None, "Ошибка при добавлении записи в базу")
        data['form']=form        
        return render(req,'product/add_product.html', data)
        
