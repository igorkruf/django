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
from .forms import AddPosts, SetType
######################################################
from django.contrib.auth.mixins import LoginRequiredMixin
##########################################################
import datetime
from django.forms import formset_factory
from posts.forms import ArticleForm
ArticleFormSet = formset_factory(ArticleForm)
##########################################################


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
        formset = ArticleFormSet(
        # initial=[
        #          {
        #              "title": "Django is now open source",
        #              "pub_date": datetime.date.today(),
        #          }
        #      ]
         )
        data={}
        data['title']="New заголовок"
        data['form']= AddPosts() 
        data['formset']=formset        
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
    

class AddType(LoginRequiredMixin, View):

    def get(self, req, *args, **kwargs):
        data={}
        data['title']="Новый тип"
        data['form']= SetType() 
        # data['formset']=formset        
        return render(req, 'posts/add_type.html', data)

