```
class  Entry ( models . Model ): 
    LIVE_STATUS  =  1 
    DRAFT_STATUS  =  2 
    HIDDEN_STATUS  =  3 
    STATUS_CHOICES  =  ( 
        ( LIVE_STATUS ,  'Live' ), 
        ( DRAFT_STATUS ,  'Draft' ), 
        ( HIDDEN_STATUS ,  'Hidden' ), 
    ) 
    # ...здесь есть еще несколько полей... 
    status  =  models . IntegerField ( choices = STATUS_CHOICES ,  default = LIVE_STATUS 
```

Однако мы можем просто определить набор констант:

```
LIVE_STATUS  =  1 
DRAFT_STATUS  =  2 
HIDDEN_STATUS  =  3
```
И отсюда мы можем переопределить STATUS_CHOICESкортеж, чтобы он опирался на эти константы:

```
STATUS_CHOICES  =  ( 
    ( LIVE_STATUS ,  'В прямом эфире' ), 
    ( DRAFT_STATUS ,  'Черновик' ), 
    ( HIDDEN_STATUS ,  'Скрытый' ), 
)
```
И все, кому требуется фильтровать текущие записи, может использовать его:

```
live_entries = Entry.objects.filter(status=LIVE_STATUS)
```
