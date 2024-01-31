<code>
   {% extends 'public/index.html' %}
  
  {% block title %}
      {{title}}
      {% endblock title %}
  
  {% block main__content %}
   <div class="form__wrapper add_set_type">
  <form class="form "  method="post">
     <h1>Добавление коплектующих к {{type.name}}</h1>
  {{form.non_field_errors}}
  {% csrf_token %} 
  {% comment %}  {% endcomment %}
  <div class="field_row"><label class="form__label" for="{{f.id_for_label}}">Тип комплектующих</label>
  <select class="input" data-type_id={{type.id}} name="part1" >
  <option >Выбери блок</option>
  {% for type1 in list_types_for_part %}
  <option value="{{type1.id}}">{{type1.name}}</option>
  {% endfor %}
  </select>
  </div>
      <div class="form__error">{{f.errors}}</div>
  
  {% comment %}  {% endcomment %}
  {% for  f in form %}
  <div class="field_row"><label class="form__label" for="{{f.id_for_label}}">{{f.label}}</label>{{f}}</div>
      <div class="form__error">{{f.errors}}</div>
  {% endfor%} 
  <button class="input" type="submit">Добавить в set</button>
  </form>
  {% comment %} <template>
  {{form_add_key_value}}
  <button class="updatelist">Добавить запчасть</button
   </template> {% endcomment %}
  </div>
  
  {% endblock main__content%}

</code>
<code>
      let addSetType=document.querySelector('.add_set_type');
   
   if (addSetType){
       let type=addSetType.querySelector("[name='type']");
       let part=addSetType.querySelector("[name='part']");
       
       let selPart=addSetType.querySelector("[name='part1']");
       selPart.addEventListener("change", function(){
           type.value=selPart.dataset.type_id;
           part.value=selPart.value;
       
       });
   }
</code>



<code>
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
        
</code>
