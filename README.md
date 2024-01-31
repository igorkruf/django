


* Получаем список типов у которых присутствуют запчасти (part) данного типа
<code>
   list_exclude=[]
   list_dict_collection_types=collection_types.values("type", "part");
   for dict_collection_types in list_dict_collection_types:
      if  dict_collection_types['part']==tupe_id:
         list_exclude.append(dict_collection_types['type'])
</code>


* Нужно получить список типов без исходного
<code>
   QuerySet: colection_types=SetType.objects.exlude(pk=type_id).exclude(pk__in=list_exclude).
</code>
    


  
