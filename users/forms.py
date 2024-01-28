from django import forms
from django.contrib.auth import get_user_model
import json
from .models import UserProfile


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


list_manufacturer=[
    {
        "id":1,
        "name":"Собственное изготовление",
    },
    {
        "id":2,
        "name":"Название фирмы 1",
    },
    {
        "id":3,
        "name":"Название фирмы 2",
    },

] 


class UserProfileForm(forms.ModelForm):
    # users_model= get_user_model()
    # users=forms.ModelChoiceField(users_model.objects.all(), empty_label="(Nothing)")
    # kol_vo= forms.IntegerField()
    class Meta:
        model=UserProfile
        fields=["info_user", "dr", "foto"]
        widgets={
            'info_user':forms.Textarea(attrs={"class":"input"}),
            'dr':forms.TextInput(attrs={"class":"input datepicker"}),
            'foto':forms.ClearableFileInput(attrs={"class":"input"})
        }  
        labels={
            'info_user':'Дополнительная информация',
            'dr':'Дата рождения',
            'foto': 'Ваша фотография'
        }
    


   


   
# if __name__=="__main__":

#     ddd= {'key1':'value1', 'key2':'value2'}
#     ooo= json.dumps(ddd)
#     print(ooo)



