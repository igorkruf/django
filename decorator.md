### view.py
```
from .utils import in_group


@in_group(list_required_groups=["student"])        
def get_function_view(req, *args, **kwargs):
    return render(req, 'stories_app/function.html')
```
### utils.py
```
from  django.shortcuts import  render

def in_group(list_required_groups=[]):
    def decorator(func):
        def wrapper(req, *args, **kwargs):
            list_user_groups=list(req.user.groups.all().values_list('name', flat=True))
            for group in list_required_groups:
                if group in list_user_groups:
                    return func(req, *args, **kwargs)
                
            return render(req, "stories_app/test.html")    

        return wrapper
    return decorator
```
