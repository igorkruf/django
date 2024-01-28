from django.urls import reverse
from django import template
from public import views as public_views
from django.contrib.auth.models import User
from users.views import user_menu





register=template.Library()

@register.simple_tag()
def get_users():
    # return public_views.sss
    return User.objects.all().values('username', 'first_name')


@register.inclusion_tag('users/header_usermenu_nav.html')
def show_user_menu():
    return {"user_menu": user_menu }










    

