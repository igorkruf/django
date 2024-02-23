Полезные ссылки
https://django.readthedocs.io/en/latest/ref/models/querysets.html

https://docs.djangoproject.com/en/1.11/ref/models/fields/#manytomanyfield   - ManyToManyField 

https://docs.djangoproject.com/en/1.11/ref/models/fields/#foreignkey   -ForeignKey 

https://docs.djangoproject.com/en/1.11/ref/models/fields/#onetoonefield  -OneToOneField

////////////////////////////////////////////////////////////////////

Гораздо более простой вариант ответа @ s29:

Вместо настройки формы вы можете просто ограничить выбор, доступный в поле формы, с вашей точки зрения:

у меня сработало: в form.py:

class AddIncomingPaymentForm(forms.ModelForm):
    class Meta: 
        model = IncomingPayment
        fields = ('description', 'amount', 'income_source', 'income_category', 'bank_account')
в view.py:

def addIncomingPayment(request):
    form = AddIncomingPaymentForm()
    form.fields['bank_account'].queryset = BankAccount.objects.filter(profile=request.user

/////////////////////////////////////////////////////////////////////

https://translated.turbopages.org/proxy_u/en-ru.ru.17e0f863-65c3587c-728af8c2-74722d776562/https/stackoverflow.com/questions/6023421/how-to-edit-model-data-using-django-forms - форма для редактирования с предустановленными значениями изменяемого объекта!!!

https://docs.djangoproject.com/en/4.0/ref/csrf/ - fetch отправка POST форм!!!


https://sky.pro/media/kak-rabotat-s-modulem-pathlib-v-python/ - про модуль pathlib

https://youtu.be/km6tGZ3OHvQ?si=dzV0te5cd1hHAszW  - интернет магазин на django


https://youtu.be/jaeTOpCmbLA?si=U0g4pyHOrH8DoXYj - ещё про джанго
