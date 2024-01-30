menu = [
    {'title': "О сайте", 'url': 'about'},
    {'title': "Добавить статью", 'url': 'add_page'},
]

menu1=[
    {'title':'О сайте меню1', 'url': 'about'},
     {'title': "Добавить статью меню1", 'url': 'add_page'},
]


class HeaderMenu:
    @staticmethod
    def get_context_header_menu(**kwargs):
        context=kwargs
        context['header_menu']= menu
        return context   


class AsideMenu:
    @staticmethod
    def get_context_aside_menu(**kwargs):
        context=kwargs
        context['aside_menu']= menu1
        return context  
 
        

    
    
   
    

