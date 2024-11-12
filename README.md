


Получаем значение любой кукки на js
<code>
    function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + "=")) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
</code>

<code>
    // formData.append('csrfmiddlewaretoken', csrftoken);
    let response = await fetch('add/',{
        method:"POST",
        body:JSON.stringify({"name":"ddddd"}),
        headers: {
            'Content-Type': 'application/json',
                     "X-CSRFToken": csrftoken
                  },

    })

    
</code>







<code>
    from django.db.models.signals import post_save, pre_save
    
        
        @receiver(pre_save, sender=Product)
    def pre_reciver_product(sender, instance, **kwargs):
         
        if  instance.pk :
            obj=Product.objects.get(pk=instance.id)
            if instance.stage_id != obj.id:
                add_to_actions('Изменили состояние')             
        elif 1==1:
            @receiver(post_save, sender=Product)
            def post_reciver_product(sender, instance, **kwargs):
                 add_to_actions(f'добавили:{instance.id}')
        
    def add_to_actions(str='По умолчанию', ):
        print(str)
</code>


FIGMA (igor-kruf, igor-kruf@list.ru, Pervil-9)




<code>
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
</code>
<code>
@receiver(pre_save, sender=Product)
def test_recive(sender, instance, **kwargs):
    print(instance.type.name)
</code>    

<code>
    @receiver(pre_save, sender=Car)
    def car_is_saved(sender, instance, **kwargs):
    try:
        obj = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        pass
    else:
        if obj.price == instance.price:
            # Цена не изменилась
            pass
        elif obj.price < instance.price:
            # Цена поднялась
        elif obj.price > instance.price:
            # Цена снизилась
</code>


https://russianblogs.com/article/5984705908/ - listView, detailView, ...

![alt text](https://habrastorage.org/r/w1560/files/688/052/4d1/6880524d12ff4f689c0a84d1302c5715.png)      

chosen_obj = next((obj for obj in your_objects if getattr(obj, 'my_attr', None) == target_value), None)

chosen_objects = [obj for obj in your_objects if obj.my_attr == target_value]

chosen_obj = next((value for key, value in object_dict.items() if value.my_attr == target_value), None)


  
