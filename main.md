```
import itertools
from itertools import groupby

final={
  user:{
  lp:mark,
  lp:mark,
  ...
  ...
}
final_final = {}

for user, val in final.items():
  val2 = []
  for lp, mark in val.items():
    koeff = lp.lessons_from_cm.summer_koeff if lp.period_training==PeriodTraining.SUMMER else lp.lessons_from_cm.winter_koeff
    val2.append((lp.lessons_from_cm.discipline.code, mark*koeff))
  sorted(val2, lambda x: x[0])
  for key, group in groupby(val2, lambda x : x[0]):
    key_and_group = {key : sum(list(group[1]))}


```
```
list_tuple_module_m = [("M1", {1:0, 2: 33, 3:89}), ("M2", {1:34, 2: 33, 3:89})]
list_tuple_module_p = [{1:21, 3:10}]

for tuple_module_m in list_tuple_module_m:
    for key_m,val_m in tuple_module_m[1].items():
        for key_p, val_p in list_tuple_module_p[0].items():
            if key_p==key_m:
               tuple_module_m[1][key_m]= val_p 


print(list_tuple_module_m)
```
