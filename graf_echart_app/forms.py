
from django import forms
from .models import Fructes


class DateInput(forms.DateInput):
    input_type = 'date'


class FormAddFructes(forms.ModelForm):
    '''
    Форма для проверки datapicker для поля типа date
    '''
    

    class Meta:
        model=Fructes
        fields=['name', 'kolvo', 'data']
        widgets={
            'data':DateInput(format='%Y-%m-%d')
        }