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



  
