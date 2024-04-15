from django.db import models

# Create your models here.
class Fructes(models.Model):
    '''Модель для изучения echarts'''


    
    CHOICES_FRUCTES=[
        ("ya","Яблоко"),
        ("gr", "Груша"),
        ("arb", "Арбуз")
    ]

    name=models.CharField(max_length=250, choices=CHOICES_FRUCTES)
    kolvo=models.PositiveIntegerField()
    data=models.DateField()

    def __str__(self):
        return self.name