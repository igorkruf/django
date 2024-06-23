## views.py
```
from django.contrib import messages


class TestJs(ContextMixin, View):
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        return context

    def get(self, req, *args, **kwargs):
        context=self.get_context_data(**kwargs)
        return render(req, 'stories_app/test.html', context)

    def post(self, req, *args, **kwargs):
        ddd="Жопа жопная"
        messages.success(req, f"{ddd} Profile details updated.")
        return redirect('to_from_test')
    

class ToFromTest(ContextMixin, View):
    '''
    Тестирование передачи переменных через "redirect"
    '''

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        return context
    
    def get(self, req, *args, **kwargs):
        context=self.get_context_data(**kwargs)
        print('ddddddddddddd')
        return render(req, 'stories_app/to_from_test.html', context)
        
```
## base.html
```
<div class="modal__wrapper">
        <div class="modal">
            <div class="modal__btn-close">Закрыть</div>
            <div class="modal__content"> </div>
        </div>
    </div> 
    <div class="tool-tip {% if messages %} tool-tip_visible {% endif %} ">
        {% for message in messages %}
        <div {% if message.tags %} class="{{ message.tags }}"{% endif%}>{{message}}</div>
        {% endfor %}
    </div>  
```
## styles.css
```
/* tool-tip */
.tool-tip{
    position:absolute;
    top: -100px;
    right:0;
    transition: top 1s ease-in-out;
}
.tool-tip_visible{
    top: 100px;
}
.success{
    background-color: green;
    color:#fff;
}
.error{
    background-color: red;
    color:#fff;
}

```
## scripts.js скрываем nool-tip окно через 2 сек
```
let toolTip= document.querySelector('.tool-tip');
if (toolTip.classList.contains("tool-tip_visible")){
    setTimeout(function(){
        toolTip.classList.remove('tool-tip_visible')
    }, 2000)
}
```
