


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




  
