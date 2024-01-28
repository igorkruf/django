from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from .models import Post
from users.views import  user_menu
from django.contrib.auth.decorators import login_required
from django.conf import settings
from public.functions import set_activ_usermenu_item
#####################################################
from django.views import View
from .forms import AddPosts
######################################################
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# @login_required
def index(req):
    print(reverse(settings.LOGIN_URL))
    if not req.user.is_authenticated:
        return redirect(f'{reverse(settings.LOGIN_URL)}?next={req.path}')
    list_posts_by_user=Post.objects.all().filter(author_id=req.user.id)
    # 
    print(list_posts_by_user)
    data={
        "list_posts_by_user":list_posts_by_user,
        }
    

    return render(req, 'posts/index_posts.html', data ) 



def add_posts(req):
    return HttpResponse('Добавление поста')

@login_required
def del_posts(req, post_id):
    print(type(post_id))
    del_post= Post.objects.get(pk=post_id)
    if del_post.author_id==req.user.id:
        try:
            del_post.delete()
                # del_post=Post.objects.get(pk=post_id)
                    # del_post.delete()
            data={
                "status":True,
                "message":"Пост успешно удалён"         
                }
        except: 
            data={
                "status":False,
                "message":"Ошибка при удалении поста"
                }
    else:
         data={
              "status":False,
              "message":"Пытаетесь удалить чужой пост"
         }

    # data={"q":"q"}
    return JsonResponse(data)

class AddPost(LoginRequiredMixin, View):
    
    # login_url="users:login_users"
    def get(self, req, ):
        data={}
        data['title']="New заголовок"
        data['form']= AddPosts()         
        return render(req, 'posts/add_posts.html', data)
    

    def post(self, req):
        data={}
        form=AddPosts(req.POST)
        if form.is_valid():
            cd=form.cleaned_data
            print(cd)
            try:
                new_posts=Post.objects.create(**cd)
                print(new_posts.id)
                data['form']=AddPosts()
            except:
                form.add_error(None, "Ошибка при добавлении в базу данных")
                data['form']=form
        else:
            data['form']=AddPosts(req.POST)

        return render(req, 'posts/add_posts.html', data)
