from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


# Create your models here.

class Storage(models.Model):
    type=models.ForeignKey('Type', on_delete=models.PROTECT)
    


class Stage(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Actions(models.Model):
    product=models.ForeignKey('Product', on_delete=models.CASCADE)
    stage=models.ForeignKey('Stage', on_delete=models.PROTECT)
    date=models.DateTimeField()
    user=models.ForeignKey(User, on_delete=models.PROTECT, null=True)

class Product(models.Model):
    #user= models.ForeignKey(User, on_delete=models.PROTECT, null=True,)
    stage=models.ForeignKey('Stage', on_delete=models.PROTECT)
    type= models.ForeignKey('Type', on_delete=models.PROTECT)
    about=models.TextField()

    def __str__(self):
        return self.type.name


class Type(models.Model):
    name=models.CharField(max_length=255, verbose_name="Название ")
    

    def __str__(self):
        return self.name


class SetType(models.Model):
    type=models.ForeignKey('Type', on_delete=models.PROTECT, related_name='type_id')
    part=models.ForeignKey('Type', on_delete=models.PROTECT, related_name='part_id')
    kol_vo=models.IntegerField()


    class Meta:
        unique_together=['type', 'part']


    def __str__(self):
        return f'{self.type.name} - {self.part.name} : {self.kol_vo} шт' 
    

       



@receiver(pre_save, sender=Product)
def test_recive(sender, instance, **kwargs):
    print(instance.type.name)
    