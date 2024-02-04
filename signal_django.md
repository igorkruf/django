
# Это в файле  apps.py приложения
<code>
    from django.apps import AppConfig
    from django.db.models.signals import pre_save, post_save
    
    class SecondConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'second'
        def ready(self):
              from .models import MyModel, Action  # or...
              # MyModel = self.get_model('MyModel')
               def save_profile(sender, instance, **kwargs):
                     print('kasjdhfkajdshakjdsfhdfshj')
                     Action.objects.create(name_action=instance.name)
                     # registering signals with the model's string label
                post_save.connect(save_profile, sender='second.MyModel')
</code>

<code>
    def ready(self):
        
        from .models import MyModel, Action  # or...
        # MyModel = self.get_model('MyModel')
        
        def presave_profile(sender, instance, **kwargs):
            print('pre_save')
            if 1==1:
                post_save.connect(save_profile, sender='second.MyModel')
        
        
        
        def save_profile(sender, instance, **kwargs):
            print('post_save')


            Action.objects.create(name_action=instance.name)
        # registering signals with the model's string label
        
        pre_save.connect(presave_profile, sender='second.MyModel')
</code>

# Это models.py
<code>
class MyModel(models.Model):
    name=models.CharField(verbose_name="Название")

class Action(models.Model):
     name_action=models.CharField()
     date_action=models.DateTimeField(default=datetime.now())
</code>
