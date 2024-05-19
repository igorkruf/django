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
```
class TreeQuerySet(models.QuerySet):
    def with_tree_fields(self, tree_fields=True):  # noqa: FBT002
        """
        Запрашивает древовидные поля в этом наборе запросов
        Введите `False`, чтобы вернуться к набору запросов без древовидных полей.
        """
        if tree_fields:
            self.query.__class__ = TreeQuery
            self.query._setup_query()
        else:
            self.query.__class__ = Query
        return self

    def without_tree_fields(self):
        """
        Не запрашивает никаких древовидных полей в этом наборе запросов
        """
        return self.with_tree_fields(tree_fields=False)

    def order_siblings_by(self, *order_by):
        """
        Устанавливает атрибут sibling_order древовидного запроса
        Передает имена полей модели в виде списка строк
        чтобы упорядочить дерево родственных элемента по этим полям модели
        """
        self.query.__class__ = TreeQuery
        self.query._setup_query()
        self.query.sibling_order = order_by
        return self

    def tree_filter(self, *args, **kwargs):
        """
	Добавляет фильтр к древовидному запросу rank_table_query
        Принимает те же аргументы, что и Django QuerySet .filter()
        """
        self.query.__class__ = TreeQuery
        self.query._setup_query()
        self.query.rank_table_query = self.query.rank_table_query.filter(
            *args, **kwargs
        )
        return self

    def tree_exclude(self, *args, **kwargs):
        """
        Добавляет фильтр к древовидному запросу rank_table_query
        Принимает те же аргументы, что и Django QuerySet .exclude()
        """
        self.query.__class__ = TreeQuery
        self.query._setup_query()
        self.query.rank_table_query = self.query.rank_table_query.exclude(
            *args, **kwargs
        )
        return self

    def tree_fields(self, **tree_fields):
        self.query.__class__ = TreeQuery
        self.query._setup_query()
        self.query.tree_fields = tree_fields
        return self

    @classmethod
    def as_manager(cls, *, with_tree_fields=False):
        manager_class = TreeManager.from_queryset(cls)
        # Используется только при деконструкции:
        manager_class._built_with_as_manager = True
        # Установите атрибут для класса, а не для экземпляра, чтобы автоматическое создание подкласса
        #, используемое, например, для отношений, также обнаруживало этот атрибут
        #.
        manager_class._with_tree_fields = with_tree_fields
        return manager_class()

    as_manager.queryset_only = True

    def ancestors(self, of, *, include_self=False):
        """
        Возвращает предков данного узла, упорядоченных от корня дерева
        к более глубоким уровням, необязательно включая сам узел
        """
        if not hasattr(of, "tree_path"):
            of = self.with_tree_fields().get(pk=pk(of))

        ids = of.tree_path if include_self else of.tree_path[:-1]
        return (
            self.with_tree_fields()  # Поля дерева задач не являются строго обязательными
            .filter(pk__in=ids)
            .extra(order_by=["__tree.tree_depth"])
        )

    def descendants(self, of, *, include_self=False):
        """
        Возвращает потомков данного узла в порядке возрастания глубины, необязательно
        включая сам узел и начиная с него
        """
        connection = connections[self.db]
        if connection.vendor == "postgresql":
            queryset = self.with_tree_fields().extra(
                where=["%s = ANY(__tree.tree_path)"],
                params=[self.model._meta.pk.get_db_prep_value(pk(of), connection)],
            )

        else:
            queryset = self.with_tree_fields().extra(
                # ОБРАТИТЕ ВНИМАНИЕ! Представление tree_path не является частью API.
                where=[
		    # XXX Это может быть небезопасно для некоторых типов полей первичного ключа.
                    # Это, безусловно, безопасно для целых чисел.
                    f'instr(__tree.tree_path, "{SEPARATOR}{self.model._meta.pk.get_db_prep_value(pk(of), connection)}{SEPARATOR}") <> 0'
                ]
            )

        if not include_self:
            return queryset.exclude(pk=pk(of))
        return queryset

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
