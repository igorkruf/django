from django.shortcuts import render
from django.views import View
import matplotlib.pyplot as plt
import numpy as np
import io, base64
class MainPage(View):
    
    
    def get(self, req, *args, **kwargs):

        context={}
        x = np.linspace(0, 10, 50)
        y = x
        # Построение графика
        plt.title('Линейная зависимость y = x') # заголовок
        plt.xlabel('x') # ось абсцисс
        plt.ylabel('y') # ось ординат
        plt.grid() # включение отображение сетки
        plt.plot(x, y) # построение графика
        # #############################################################
        my_stringIObytes=io.BytesIO()
        plt.savefig(my_stringIObytes, format='jpg')
        my_stringIObytes.seek(0)
        my_base64_jpgData= base64.b64encode(my_stringIObytes.read()).decode()
        ################################################################
        context['plot']= my_base64_jpgData
        return render(req, 'graf_matplotlib_app/index.html', context)