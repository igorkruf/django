https://pythonist.ru/django-optimizacziya-raboty-s-bazoj-dannyh/  ссылка на сайт-источник

### Используйте постоянные соединения с базой данных

Django при каждом запросе открывает новое соединение с базой данных и закрывает его, когда его запрос выполнен.
За это поведение отвечает настройка https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-CONN_MAX_AGE-  CONN_MAX_AGE — значение по умолчанию равно 0. Но сколько секунд должно быть установлено соединение? Это зависит от трафика вашего сайта — чем больше трафика, тем больше секунд требуется для сохранения соединения. Мы бы рекомендовали установить относительно небольшое значение, например 60.

### Используйте select_related() и prefetch_related()

В Django select_related() и prefetch_related() предназначены для снижения количества запросов к базе данных. Более подробно о них вы можете прочитать https://medium.com/@goutomroy/django-select-related-and-prefetch-related-f23043fd635d .

### Используйте значения внешних ключей напрямую

Django ORM автоматически извлекает и кеширует внешние ключи, поэтому используйте их вместо ненужных запросов к базе данных.
```
# Так делать не стоит. Требуется обращение к базе данных.
blog_id = Entry.objects.get(id=200).blog.id
# Лучше так. Внешний ключ уже кеширован, поэтому обращение к базе данных не требуется.
blog_id = Entry.objects.get(id=200).blog_id
# Или так. Обращение к базе данных так же не требуется.
blog_id = Entry.objects.select_related('blog').get(id=200).blog.id
```

### Используйте count() и exists()

Если вам не нужно содержимое QuerySet, используйте count() и exists().
```
# Так делать не стоит.
count = len(Entry.objects.all()) 
# Лучше так. 
count = Entry.objects.count() 
# Так делать не стоит.
qs = Entry.objects.all()
if qs:
   pass
  
# Лучше так. 
qs = Entry.objects.exists()
if qs:
   pass
```

### Используйте delete() и update() для массовых операций

Если вы хотите удалить или обновить сразу несколько экземпляров модели, используйте соответственно delete() и update().
обрати в последней строке используем F выражение

```
# Так делать не стоит. Элементы удаляются по одному.
for entry in Entry.objects.all():
    entry.delete()
    
# Лучше так. Удаляются все сразу.
Entry.objects.all().delete()
# Так делать не стоит.
for entry in Entry.objects.all():
    entry.likes += 1
    entry.save()
    
# Лучше так.
Entry.objects.update(likes=F('likes')+1)
```
### Используйте  F-выражения
```
# Так делать не стоит.
for entry in Entry.objects.all():
    entry.likes += 1
    entry.save()
    
# Лучше так.
Entry.objects.update(likes=F('likes') + 1)
```



### Используйте values(), values_list(), defer(), only()

Если вам нужны определенные поля в результатах QuerySet и вы хотите получить результаты в списке, кортеже или словарях, используйте [values()](https://docs.djangoproject.com/en/2.1/ref/models/querysets/#values)  и [values_list()](https://docs.djangoproject.com/en/2.1/ref/models/querysets/#values-list).

Если вам нужны определенные поля в результатах QuerySet вы хотите получить  объекты модели в QuerySet вместо списка, кортежа или словарей, используйте [defer()](https://docs.djangoproject.com/en/2.1/ref/models/querysets/#defer) и [only()](https://docs.djangoproject.com/en/2.1/ref/models/querysets/#only).
