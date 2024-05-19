Полезные ссылки
https://django.readthedocs.io/en/latest/ref/models/querysets.html

https://docs.djangoproject.com/en/1.11/ref/models/fields/#manytomanyfield   - ManyToManyField 

https://docs.djangoproject.com/en/1.11/ref/models/fields/#foreignkey   -ForeignKey 

https://docs.djangoproject.com/en/1.11/ref/models/fields/#onetoonefield  -OneToOneField

https://youtu.be/XPOeKYGekNo?si=D2R-IGd_9rZ3LyrI  - ролик по отношению onetoone 

https://www.youtube.com/watch?v=Fzh9S8B7yhQ - reverse_lazy   понятное объяснение.(но не актуально)

https://sky.pro/wiki/html/sozdanie-izmenyaemykh-html-elementov-na-chistom-java-script/?ysclid=lua57dss8d169964360  -изменение размеров блоков перетаскиванием мышкой

https://youtu.be/mgldr5PIMqU?si=8J9bIZZofg7JWkhe   - права доступа!!! - интересно доходчиво !!!  обязательно попробовать ограничить доступ и организовать для суперпользователя возможность  назначать , менять 
права
////////////////////////////////////////////////////////////////////////////////////////////////////////
https://django-treebeard.readthedocs.io/en/latest/al_tree.html#module-treebeard.al_tree  Древовидная структура (в частности меню)


https://django-mptt.readthedocs.io/en/latest/admin.html  -это мне показалось доступней
///////////////////////////////////////////////////////////////////////////////////////////
https://django-tree-queries.readthedocs.io/en/latest/ - работа с древовидной структурой- вроде как этот вариант тоже приемлем!!! даже лучше чем остальные
https://github.com/feincms/django-tree-queries - github этого решения
```
# Базовое использование, полностью игнорирующее древовидную структуру.
nodes = Node.objects.all()

# Выборка узлов в порядке поиска по глубине. Все узлы будут иметь атрибуты
# tree_path, tree_ordering и tree_depth.
nodes = Node.objects.with_tree_fields()

# Извлеките любой узел.
node = Node.objects.order_by("?").first()

# Выборка прямых дочерних элементов и включение полей дерева. (Родительский внешний ключ
# указывает related_name="children")
children = node.children.with_tree_fields()

# Извлеките всех предков, начиная с корня.
ancestors = node.ancestors()

# Извлеките всех предков, включая self, начиная с корня.
ancestors_including_self = node.ancestors(include_self=True)

# Извлекаем всех предков, начиная с самого узла.
ancestry = node.ancestors(include_self=True).reverse()

# Извлеките всех потомков в порядке поиска в глубину, включая self.
descendants = node.descendants(include_self=True)

# Временно переопределить порядок по братьям и сестрам.
nodes = Node.objects.order_siblings_by("id")
```




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

https://ctrlzblog.com/how-to-use-the-many-to-many-field-in-your-django-models/    -  many to many

https://www.codecamp.ru/blog/matplotlib-save-figure/?ysclid=lurdke2elt498890158 - как сохранить фото графика matplotlib
