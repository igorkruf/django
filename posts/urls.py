from django.urls import path
from . import views


app_name="posts"

urlpatterns = [
    path('', views.index, name="index_posts"),
    path('add/', views.AddPost.as_view(), name="add_posts"),
    path('<int:post_id>/del/', views.del_posts, name="del_posts")
]