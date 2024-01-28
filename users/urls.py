from django.urls import path
from . import views


app_name="users"

urlpatterns = [
    path('', views.index, name="index_users"),
    path('registration/', views.add_user, name="registration_users"),
    path('login/', views.login_user, name="login_users" ),
    path('logout/', views.logout_user, name="logout_users"),
    path('profile/', views.profile_user, name="profile_users")
]