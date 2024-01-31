* Нужно получить список типов без исходного
<code>
QuerySet: colection_types=SetType.objects.exlude(pk=type_id)
</code>


* Получаем список типов у которых присутствуют запчасти (part) данного типа
<code>
list_dict_collection_types=collection_types.values("type", "part");

for dict_collection_types in list_dict_collection_types:






</code>
    


  
