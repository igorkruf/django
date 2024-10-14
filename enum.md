```
from enum import Enum


class ExtendedEnum(Enum):

    @classmethod
    def select_list(cls):
        return [(period.value[0], period.value[1]) for period in TrainingPeriod]


class TrainingPeriod(ExtendedEnum):
    WINTER=(1, 'Зима')
    SUMMER=(2,'Лето')
```
```
from enum_2 import TrainingPeriod


print(TrainingPeriod.select_list())   
       
```
