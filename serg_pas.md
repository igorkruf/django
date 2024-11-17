[Про markdawn](https://gist.github.com/Jekins/2bf2d0638163f1294637)

### lessons_plan/assets/scripts_style/scripts.js

стр 376 - для обработки клика при выборе занятия во время составления расписания

### lessons_plan/forms.py 
-добавил скрытое поле lesson_from_cm в форму (AddLessonsPlanForm)

```
class AddLessonPlanForm(forms.ModelForm):
    '''
    Форма добавления/редактирования записи в модель LessonPlan
    '''
    place=TreeNodeChoiceField(Place.objects.all(), empty_label="Выберите место проведения", widget=forms.Select(attrs={"class":"form-field"}), label="Место проведения" )
    discipline=forms.ModelChoiceField(DisciplineName.objects.all(), empty_label="Выбери предмет подготовки", widget=forms.Select(attrs={"class":"form-field select-discipline-for-manual-lesson"}), label="Предмет подготовки", required=False)
    lesson=SelectThemelessonModelChoiceField(Lesson.objects.all(), empty_label="Выберите занятиe", widget=forms.Select(attrs={"class":"form-field open-sub-modal lesson-from-bp display-none", "onmousedown":"(function(e){ e.preventDefault(); })(event, this)" ,"data-url":"/lessons_plan/add/select-theme-of-lesson/"}), label="Занятие", required=False)
    period_training=forms.IntegerField(widget=forms.RadioSelect(attrs={"class":"form-field period-training form-field__period-training content_inline"}, choices=PeriodTraining.PERIOD_TRAINING_CHOICES), label="Период обучения")

    class Meta:
        model=LessonPlan
        fields=["date", "period_training", "lesson_from_cm",  "academic_hours", "subdivision", "sub_subdivision", "type_lesson",  "place",  "specialist_groups", "from_bp", "lesson", "discipline", "manual_lesson", "standard_tasks", "provision", "teacher"]
        labels={
            "date":"Дата",
            "subdivision":"Подразделения",
            "sub_subdivision": "Под подразделение",
            "specialist_groups":"Группы специалистов",
            "academic_hours":"Время",
            "from_bp":"По программе боевой подготовки",
            "teacher":"Руководитель",
            "manual_lesson":"Ручной ввод темы занятия",
            "standard_tasks":"",
            "provision":"Материально-техническое обеспечение",
            "type_lesson":"Тип занятия",
            # "period_training":"Период обучения"
        }
        widgets={
           "date":forms.HiddenInput(attrs={"class":"form-field "}),
            "subdivision":forms.HiddenInput(),
            "sub_subdivision":forms.HiddenInput(),
            "lesson_from_cm":forms.HiddenInput(),
            "specialist_groups":forms.CheckboxSelectMultiple(attrs={"class":"form-field form-field__check-box_incolumn form-field__check-box"}),
            "academic_hours":forms.CheckboxSelectMultiple(attrs={"class":"form-field form-field__check-box_incolumn form-field__check-box"}),
            "teacher":forms.Select(attrs={"class":"form-field"}),
            "type_lesson":forms.Select(attrs={"class":"form-field form-field__type-lesson", }),
            "from_bp":forms.CheckboxInput(attrs={"class":"form-field from-bp-check form-field__check-box"}),
            "manual_lesson":forms.Textarea(attrs={"class":"form-field manual-lesson display-none"}),
            "standard_tasks":forms.CheckboxSelectMultiple(attrs={"class":"form-field1 form-field__check-box_incolumn form-field__check-box check-box_standard_task", "required":"False"}),
            "provision":forms.Textarea(attrs={"class":"form-field provision form-field__provision"}),
            # "period_training":forms.RadioSelect(attrs={"class":"form-field period-training form-field__period-training content_inline"})
        }


```

### lessons_plan/views.py 

в этом классе надо получить list где в элементе связать занятия компетен... и плана БП 

```
class GetListLessonOfTheme(View):
    '''
    Список занятий выбранной темы
    '''

    def get(self, req, *args, **kwargs):
        context={}
        context['theme']=Theme.objects.get(pk=kwargs['theme_pk'])
        print('\n'*3)
        print(context['theme'].discipline.number)
        #список занятий темы из ПБП
        list_lesson_of_theme_from_pbp=Theme.objects.get(pk=kwargs['theme_pk']).lessons.all()
        print('список занятий из пбп по данной теме: ', list_lesson_of_theme_from_pbp)
        list_lesson_of_theme_from_cm=CompetencyLesson.objects.filter(discipline_code=context['theme'].discipline.number, theme_code=context['theme'].number)
        print('список занятий из компетентосной модели по данной теме: ', list_lesson_of_theme_from_cm)

        list_lesson_of_theme=render_to_string('lessons_plan/fetch/select_lesson_of_theme.html', context, req)
        return JsonResponse({"list_lesson_of_theme":list_lesson_of_theme})
```
