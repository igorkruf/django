### ссылки на примеры
https://habr.com/ru/articles/313764/  

https://pocoz.gitbooks.io/django-v-primerah/content/glava-4-sozdanie-social-website/registratsiya-polzovatelei-i-profili-polzovatelei/rasshirenie-modeli-user.html

```
# view.py

class LoginUser(ContextMixin, View):
    '''
    Вход на сайт
    '''


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        return context


    def get(self, req, *args, **kwargs):
        context=self.get_context_data()
        form=UserLoginForm()
        context['form']=form
        return render(req, "stories_users/user_login_form.html", context)
    

    def post(self, req, *args, **kwargs):
        context=self.get_context_data()
        form=UserLoginForm(req.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(req, username=cd['username'], password=cd['password'] )
            if user and user.is_active:
                login(req, user)
                if 'next' in req.GET:
                    return redirect(req.GET['next'])
            return redirect('main_page')
        context['form']=form
        return render(req, "stories_users/user_login_form.html", context)            


class LogoutUser(ContextMixin, View):
    '''Выход'''


    def get(self, req, *args, **kwargs):
        logout(req)
        return redirect('main_page')
```
```
# form.py
from django import forms
from django.contrib.auth import models 



class UserRegisterForm(forms.ModelForm):
    # username=forms.CharField(label="Логин")
    # password=forms.CharField(label="Пароль")
    password2=forms.CharField(label="Подтверждение пароля")
    class Meta:
        model = models.User
        fields = ["username", "password", "password2", "first_name", "last_name",]
        widgets={
            "username":forms.widgets.TextInput(attrs={"class":"input"}), 
            "password":forms.widgets.PasswordInput(attrs={"class":"input"}),

        }
        labels={
            'username': 'Логин',
            'first_name':"fnnnnnnnn",
            'last_name':"lnnnnn"
        }

       




class UserLoginForm(forms.Form):
    username=forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class':'input'}))
    password=forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class':'input'}))


```
