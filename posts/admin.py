from django.contrib import admin
from .models import Post, Type, SetType

# Register your models here.
admin.site.register(Post)
admin.site.register(Type)
admin.site.register(SetType)