добавляем модели:
```
class Event():
  ```
  Поля общие для всех событий
  ```
  date
  place
  start_time
  end_time
  teacher


class fz(Event):
  ```
  event физическое воспитание 
  ```
  name_fz
  type

class OGP(Event):
  ```
  event типа огп
  ```
  name_ogp

class Phd(Event):
  ```
  event типа событие парко-хозяйственного
  дня(сюда можно добавить "по плану ПХД", помывка личного состава,
  помывка личного состава и замена нательного белья, )
  ```
  name_phd

class Weekend(Event):
  ```
  event типа событие выходного дня ("по плану выходного дня", час солдатского письма ...)
  ```
  name_weekend

```


