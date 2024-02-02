


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




  
