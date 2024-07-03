
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


# Ещё вариант  apps.py
```
from django.apps import AppConfig
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    
    def ready(self):
        # importing model classes
        from django.contrib.auth.models import User
        from .models import UserProfile
        
        @receiver(pre_save, sender=User)
        def pre_update_model(sender, **kwargs):
    
            # check if the updated fields exist and if you're not creating a new object
            if not kwargs['update_fields'] and kwargs['instance'].id:
                # Save it so it can be used in post_save
                kwargs['instance'].old = User.objects.get(id=kwargs['instance'].id)


        @receiver(post_save, sender = User)
        def add_score(**kwargs):
            if kwargs['created']:
                new_profile = UserProfile(user=kwargs['instance'])
                print('создали профиль')
                new_profile.save()
            else:
                
                print('изменяем пользователя')
                instance=kwargs['instance']
                # Add updated_fields, from old instance, so the method logic remains unchanged
                if not kwargs['update_fields'] and hasattr(instance, 'old'):
                    kwargs['update_fields'] = []
                    ddd=instance.old
                    for attr in dir(ddd):
                        print(getattr(ddd, attr))
                        
                    #         kwargs['update_fields'].append(key)
                    print(f'изменённые поля:{kwargs['update_fields']}')
```

