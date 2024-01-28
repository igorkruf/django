from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=255, verbose_name="Заголовок поста" )
    content=models.TextField(verbose_name="Текст поста")
    author=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор поста", default=1, null=True, blank=True )



    def __str__(self):
        return f'{self.title}'
    

class TypeProduct(models.Model):
    name=models.CharField()
    type_zapchast=models.ManyToManyField('TypeZapchast', through="ListTypeZapchastTypeProduct")


class TypeZapchast(models.Model):
    name=models.IntegerField()


class ListTypeZapchastTypeProduct(models.Model):
    type_product=models.ForeignKey('TypeProduct', on_delete=models.CASCADE)
    type_zapchast=models.ForeignKey('TypeZapchast', on_delete=models.CASCADE)
    kol_vo=models.IntegerField()

