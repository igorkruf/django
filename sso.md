my_overrides.py

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
