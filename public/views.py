from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views import View


# from django.contrib.auth.decorators import login_required
# Create your views here.

def index(req):

    
        
    return render(req,'index.html')



    

 