from django.shortcuts import render
from django.views import View
from graf_chart_app.models import Sales
from .forms import FormAddFructes
from graf_echart_app.models import Fructes
import pandas as pd  
# Create your views here.


class MainPage(View):
    '''
    Главная страница
    '''
    LIST_GOTOVNOST=[
        {"name":"Готовность 1", "1":1.07, "2": 2.54, "3":4.53, "4":8.94, "5":15.27, "6":33.52, "7":46.31, "8":67.82, "9":85.72, "10":100.00},
        {"name":"Готовность 2", "1":1.07, "2": 2.15, "3":3.01, "4":4.40, "5":6.67, "6":12.71, "7":20.34, "8":29.02, "9":33.43, "10":33.64},
        {"name":"Готовность 3", "1":0.00, "2": 0.39, "3":1.52, "4":4.55, "5":8.60, "6":20.80, "7":25.97, "8":38.80, "9":52.2, "10":66.36}
    ]

    def get(self, req, *args, **kwargs):
        context={}
        list_sources=[]
        data_header=list(self.LIST_GOTOVNOST[0].keys())
        list_sources.append(data_header)
        print(list_sources)
        for list_series_item in self.LIST_GOTOVNOST:
            list_series_data=list(list_series_item.values())
            list_sources.append(list_series_data)
        print(list_sources)

        # context['data_x']=data_x #Список значений по оси X для LINE графика
        # for series_item in self.LIST_GOTOVNOST:
        #     series_dict={}
        #     series_dict['name']=series_item['name']
        #     series_dict['type']='line'
        #     series_dict['data']=list(series_item.values())[1:]
        #     series_dict['label']= {}
        #     series_dict['label']['show'] = 'true'
            
        #     list_series.append(series_dict)
        # context['data_x']=data_x
        # context['list_series']=list_series

        context['list_sources']=list_sources
        return render(req, 'graf_echart_app/index.html', context)
    

class AddFructes(View):
    
    
    def get(self, req, *args, **kwargs):
        context={}
        context['form']= FormAddFructes()

        return render(req, 'graf_echart_app/add_fructes.html', context)
