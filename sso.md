my_overrides.py (client)
```
from django_sso.sso_service.backend import EventAcceptor, acceptor
from typing import * 
# В случае, когда вам нужно что-то сделать после деаутентификации 
class  MyEventAcceptor ( EventAcceptor ): 
    @acceptor  # Каждый метод акцептора событий должен быть украшен этим 
    def deauthenticate(self, user_identy): 
        # Здесь вы можете совершать свои действия перед деаутентификацией 
        print('sssssssssssssssssssssssssss sssssssssssssss')
        super().deauthenticate(user_identy) 
        # И здесь вы можете выполнять свои собственные действия после деаутентификации 
        print('sssssssssssssssssssssssssss sssssssssssssss')
    
    @acceptor  # Каждый метод акцептора событий должен быть украшен этим 
    def delete_user(self, user_identy: str):
        print('delete_user')
        super().delete_user(user_identy)

    @acceptor
    def update_account(self, fields: dict):
        print('update_account')
        print(fields)
        super().update_account(fields)
        

    @acceptor
    def update_fields(self, user_identities: List[str], fields: dict):
        print('update_fields')
        print(user_identities)
        print(fields)
        super().update_fields(user_identities, fields)
```

apps.py(server)
```
from django.apps import AppConfig
from django.db.models.signals import post_save
from django.dispatch import receiver

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        from django.contrib.auth import get_user_model
        User=get_user_model()
        from .models import UserProfile

        @receiver(post_save, sender=User )
        def add_user_profile(sender, instance, created, **kwargs):
            if created:
                UserProfile.objects.create(user=instance)
                print("Request finished!")

```
settings.py (client)
```
import os
from pathlib import Path
from dotenv import load_dotenv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path =  BASE_DIR / '.env'
if dotenv_path.exists():
    load_dotenv(dotenv_path)

LOGIN_URL = '/login/'
SSO = {
    # Specify SSO server base url (REQUIRED)
    'ROOT': 'http://127.0.0.1:8000',
    
	# Specify application token obtained in the SSO server admin panel (REQUIRED)
	'TOKEN': 'Ucj4vCp9Y4JfuYkaHc60U6kTYAy9nJayvbZ5v0NRemgpamXd5ZHv9CnzLDHuuEReUrmzdCnl8AwuR2t9XuPjzWVie5Kopbhf7pjYZgEWw7yMgc6KJotfQ7cISNYh09Be',
 	
    # Overriding event acceptor class (OPTIONAL). For more details read
    # "Overriding event acceptor in subordinated service" partition
    'EVENT_ACCEPTOR_CLASS': 'sso_client1.my_overrides.MyEventAcceptor'
}

```
