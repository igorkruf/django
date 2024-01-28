from users.views import user_menu


def set_activ_usermenu_item(id):
    for menu_item in user_menu:
        if menu_item.id==id:
            menu_item.active=True
        else:
            menu_item.actuive=False

    return user_menu 
