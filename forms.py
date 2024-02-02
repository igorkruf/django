from django import forms


from .models import Stage, Type, Storage, SetType,Product


class AddTypeForm(forms.ModelForm):
    
    class Meta:
        model=Type
        fields=["name"]
        widgets={
            "name":forms.TextInput(attrs={"class":"input"}) 
        }


class AddSetTypeForm(forms.ModelForm):
    kol_vo=forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={"class":"input", "placeholder":"Введи количество"}), label="Колличество")
    class Meta:
        model=SetType
        fields=['kol_vo', 'type', 'part']
        widgets={
            # "kol_vo": forms.NumberInput(attrs={"class":"input"}),
            "type":forms.HiddenInput(attrs={"class":"hidden_type"}),
            "part":forms.HiddenInput(attrs={"class":"hidden_part"}),
        }
        labels={
            # "kol_vo": "Кол-во",
            "type":" ",
            "part":" ",

        }

class AddProductForm(forms.ModelForm):
   
   type=forms.ModelChoiceField(Type.objects.all(), empty_label="(Выбери тип)", widget=forms.Select(attrs={"class":"input"}), label="Тип продукта" )
   stage= forms.ModelChoiceField(Stage.objects.all(), empty_label="(Установи состояние)", widget=forms.Select(attrs={"class":"input"}), label="Состояние", initial=1)
   class Meta:
       model=Product
       fields=["type", "stage", "about"]
       
