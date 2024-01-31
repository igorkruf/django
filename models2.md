<code>
    from django.db import models
    from django.contrib.auth.models import User
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
        user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    class Product(models.Model):
        stage=models.ForeignKey('Stage', on_delete=models.PROTECT)
        type= models.ForeignKey('Type', on_delete=models.PROTECT)
        def __str__(self):
            return self.stage
    class Type(models.Model):
        name=models.CharField(max_length=255, verbose_name="Название ")
        set=models.ManyToManyField('self', through="SetType")
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
</code>
