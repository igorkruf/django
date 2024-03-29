from django import forms
from django.contrib.auth import get_user_model
from .models import Post, SetType, Type
from django.forms import formset_factory



class FormRegisterUser(forms.ModelForm):
    
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"input"}), label="Пароль ещё раз")


    class Meta:
        model=get_user_model()
        fields=["username", "password", "password2", "first_name", "last_name"]
        widgets={
            "username": forms.TextInput(attrs={"class":"input"}),
            "password": forms.PasswordInput(attrs={"class":"input"}),
            "first_name": forms.TextInput(attrs={"class":"input"}),
            "last_name": forms.TextInput(attrs={"class":"input"}),
        }
        labels={
            "username": "Login",
            "password": "Пароль",
            "password2": "Пароль ещё раз",
        }



class FormLoginUser(forms.Form):
    username=forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class':'input'}))
    password=forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class':'input'}))



class AddPosts(forms.ModelForm):
        

    class Meta:
        model=Post
        fields=["title", "content"]
        labels={
            "title":"Заголовок поста",
            "content":"Содержание",
            
            
        }
        widgets={
            "title":forms.TextInput(attrs={"class":"input"}),
            "content":forms.Textarea(attrs={"class":"input"}),
            
            
        }





# class FormLoginUser(forms.ModelForm):


#     class Meta:
#         model=get_user_model()
#         fields=["username", "password"]
#         widgets={
#             "username": forms.TextInput(attrs={"class":"input"}),
#             "password": forms.PasswordInput(attrs={"class":"input"}),
#             }
#         labels={
#             "username": "Login",
#             "password": "Пароль",
#             }


class ArticleForm(forms.Form):
    title=forms.CharField()
    pub_date=forms.DateField()


class SetType(forms.ModelForm):


    class Meta:
        model=SetType
        fields=['type_id', 'part_id', 'kol_vo']
        widgets={
            "type_id":forms.HiddenInput(),
            "part_id":forms.Select(attrs={"class":"input"}, choices=Type.objects.all().values('id', 'name')),
            "kol_vo":forms.NumberInput(attrs={"class":"input"})
        }
        labels={
            "type_id": "",
            "part_id": "Название комплектующего",
            "kol_vo": "Колличество"
        }
