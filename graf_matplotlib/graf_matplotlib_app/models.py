from django.db import models

# Create your models here.


class MyModel(models.Model):
    '''jhgsdjhgsdjgs'''


    name_student = models.CharField(max_length=250)
    ocenka=models.IntegerField()


    def __str__(self):
        return self.name_student