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
