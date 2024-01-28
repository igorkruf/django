from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FormRegisterUser, FormLoginUser, UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import time
import json

# Create your views here.


def index(req):
    print(f'jhghgjhgjhhgjhg {req}')
    return HttpResponse(f'index пользователи {req.user.username}')


user_menu= [
    {
        "id":1,
        "name":"Мои посты",
        "url":"posts:index_posts",
        "active":False
    },
    {
        "id":2,
        "name":"Мой профиль",
        "url":"users:profile_users",
        "active":False

    }
 ]



def add_user(req):
    if req.method=="POST":
        form=FormRegisterUser(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            if form.cleaned_data['password']== form.cleaned_data['password2']:
                del form.cleaned_data['password2']
                if User.objects.create_user(**form.cleaned_data):
                    print('Ты зарегистрирован!!!')
                    return redirect('users:login_users')

 
            else:
                form.add_error('password2', 'Пароли не совпадают')
                
    else:
        form=FormRegisterUser()

    return render(req, 'users/add_user.html', {"form_add_user":form})

def login_user(req):
    # print(f'Имя пользователя: {req.user.__dict__.username}')
    if req.method=="POST":
        # print(req.POST)
        # parts={}
        # parts[req.POST['users']]=req.POST['kol_vo']
        # print(type(parts))
        # parts_json=json.dumps(parts)
        # print(type(parts_json))
        # if Product.objects.create(name_product=req.POST['name_product'], users_product=parts_json):
        #     print('Всё неплохо')
        #     query_user= Product.objects.get(pk=5).users_product
        #     print(type(query_user))
        #     dict_user=json.loads(query_user)
        #     print(type(dict_user))
        #     print(dict_user['1'])
        form=FormLoginUser(req.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request=req, username=cd['username'], password=cd['password'])

            if  user and user.is_active:
                login(req, user)
                if 'next' in req.GET:
                    return redirect(req.GET['next'])
                return redirect('home')
            else:
                form.add_error(None, "Неправильный логин или пароль")        
    else:
        form=FormLoginUser()
   
    return render(req, 'users/login_user.html', {"form_login_users":form})
    # return render(req, 'users/login_user.html', {"test_form":form2})

def logout_user(req):
    logout(req)
    return redirect('users:login_users')

@login_required
def profile_user(req):
    print('Загружаем форму профиля')

    return render(req, 'users/profile_user.html',{"user_id":req.user.id, "user_profile_form": UserProfileForm})



