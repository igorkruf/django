http://kilsen.github.io/calendar/tutorial.html

https://github.com/nhn/tui.calendar

https://www.geeksforgeeks.org/how-to-create-a-dynamic-calendar-in-html-css-javascript/ 

https://djangosnippets.org/snippets/2464/

+ объяснение здесь  

https://williambert.online/2011/06/django-event-calendar-for-a-django-beginner/  

```
from calendar import *
import locale
locale.setlocale(locale.LC_ALL, '')
```
https://alexpnt.github.io/2017/07/15/django-calendar/    - интересный но не оченьхотя...

views.py
```
def get(self, req, *args, **kwargs):
        context=self.get_context_data()
        datetime_today=datetime.now()
        month= int(req.GET.get('month')) if req.GET.get('month') else datetime_today.month
        year= int(req.GET.get('year'))   if req.GET.get('year') else datetime_today.year
        my_year = int(year)
        my_month = int(month)
        # Calculate values for the calendar controls. 1-indexed (Jan = 1)
        my_previous_year = my_year
        my_previous_month = my_month - 1
        if my_previous_month == 0:
            my_previous_year = my_year - 1
            my_previous_month = 12
            my_next_year = my_year
            my_next_month = my_month + 1
        if my_next_month == 13:
            my_next_year = my_year + 1
            my_next_month = 1
        #my_year_after_this = my_year + 1
        #my_year_before_this = my_year - 1
        
        
        calendar=EventCalendar()
        
        cal=calendar.formatmonth(year, month, my_previous_month, my_next_month,  my_previous_year, my_next_year)
        context['calendar']=cal
        


        return render(req, 'board/calendar_page.html', context)
```

