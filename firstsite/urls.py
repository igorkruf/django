"""
URL configuration for firstsite project.

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
from posts import urls as posts_urls
from users import urls as users_urls
from public import urls as public_urls


urlpatterns = [
    path('', include(public_urls)),
    path('admin/', admin.site.urls),
    path('posts/', include(posts_urls, namespace="posts")),
    path('users/', include(users_urls, namespace="users"))
]
