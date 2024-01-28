from django import template


post_menu=[
        {
            "id":1,
            "name":"Редактировать",
            "url":"",
            "slug":"edit_post"
        },
        {
            "id":2,
            "name":"Удалить",
            "url":"",
            "slug":"del_post"
        },
            ]


register=template.Library()


@register.simple_tag()
def get_post_menu():
    # return public_views.sss
    return post_menu

@register.filter('filter_first_my134')
def filter_first_my(v):
    return v[0:1].lower() + v[1:2].upper()+v[1:].lower()
# @register.inclusion_tag('users/header_usermenu_nav.html')
# def show_post_menu_item():
#     return {"user_menu": user_menu}