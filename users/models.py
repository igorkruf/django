from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    info_user=models.TextField(verbose_name="Дополнительная информация")
    dr=models.DateField()
    foto=models.ImageField()
    
# class Product(models.Model):
#     users_product=models.JSONField()
#     name_product=models.CharField()  


