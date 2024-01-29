from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=255, verbose_name="Заголовок поста" )
    content=models.TextField(verbose_name="Текст поста")
    author=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор поста", default=1, null=True, blank=True )



    def __str__(self):
            return f'{self.title}'
    

    # class Storage(models.Model):
    #     type=models.ForeignKey('Type', on_delete=models.PROTECT)
        
        
    # class Stage(models.Model):
    #     name=models.CharField(max_length=255)
        
        
    # class Actions(models.Model):
    #     product=models.ForeignKey('Product', on_delete=models.CASCADE)
    #     stage=models.ForeignKey('Stage', on_delete=models.PROTECT)
    #     date=models.DateTimeField()
    #     user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
        
    # class Product(models.Model):
    #     stage=models.ForeignKey('Stage', on_delete=models.PROTECT)
    #     type= models.ForeignKey('Type', on_delete=models.PROTECT)
        
        
class Type(models.Model):
    name=models.CharField(max_length=255, verbose_name="Название ")
        
        
    def __str__(self):
        return self.name
        
                
class SetType(models.Model):
    type_id=models.ForeignKey('Type', on_delete=models.PROTECT, related_name="type_id")
    part_id=models.ForeignKey('Type',on_delete=models.PROTECT, related_name="part_id")
    kol_vo=models.PositiveIntegerField()


    class Meta:
        unique_together = ['type_id', 'part_id']
             


    