### template modal(popup window)
```
# .html

 <div class="modal__wrapper">
        <div class="modal">
            <div class="modal__btn-close">Закрыть</div>
            <div class="modal__content"> </div>
        </div>
    </div>   
     
```
### Style...
```
# .css
*{
    box-sizing: border-box;
}
body, html{
    padding:0;
    margin:0;
}
/* Общие стили */
.btn{
    display:inline-block;
    padding: 12px 24px;
    border:1px solid black;
    border-radius: 6px;
    cursor:pointer;
}

/* стили модального окна */
.modal__wrapper{
    visibility: hidden;
    opacity:0;
    transition:visibility 0.3s linear,opacity 0.3s linear;
    position:fixed;
    display:flex;
    justify-content: center;
    align-items: center;
    top:0;
    left:0;
    height: 100dvh;
    width:100vw;
    padding:24px;
    background-color: rgba(0, 0, 0, 0.5);

}
.modal{
    position:relative;
    padding:24px;
    padding-top: 48px;
    background-color: #fff;
    max-height: 100%;
    max-width: 700px;
    overflow-y: auto;
}

.modal__wrapper_visible{
    visibility: visible;
    opacity:1;
}

.modal__btn-close{
    position:absolute;
    border:1px solid black;
    padding:6px;
    border-radius: 6px;
    top:12px;
    right:12px;
    cursor:pointer;
}
```
### js появление и скрытие модального окна(см html и css выше)
```
console.log('прикрепили скрипты!!!')
let modalContent=document.querySelector('.modal__content')
let wrapperModal=document.querySelector('.modal__wrapper');
// let btnOpenModal=document.querySelector('.btn_modal_visible');
let btnCloseModal=document.querySelector('.modal__btn-close')
// закрываем модальное окно по клику по фону за пределами modal
wrapperModal.addEventListener('click', function(e){
    if (e.target==this || e.target==btnCloseModal) {
        wrapperModal.classList.remove('modal__wrapper_visible')
    }
})
```



### View подтверждения удаления
```
# view
class StoriesDelete(PermissionRequiredMixin, LoginRequiredMixin, View):
    '''Удаление объявления'''

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = {}
        context["id_stories"] = kwargs['stories_id']
        return context
    

    permission_required=["stories_app.delete_stories"]

    def get(self, req, *args, **kwargs):
        '''Отправляем форму подтверждения удаления'''

        context=self.get_context_data(**kwargs)
        # Получаем строку url
        context['action']=req.path 
        # req передаем что-бы сработал тэг {% csrf_token %} 
        template=render_to_string('stories_app/fetch/confirmation.html', context, req)
        return JsonResponse({'template':template})
        
    def post(self, req, *args, **kwargs):
        '''Удаляем запись'''

        try:
            Stories.objects.get(pk=kwargs['stories_id']).delete()
        except:
            print('ошибка при удалении истории')
        return redirect('admin_stories')

```
### js подтверждения удаления
```
let storiItemLinkDel=document.querySelectorAll('.stori-item__link_del');
storiItemLinkDel.forEach((elem)=>{
    elem.addEventListener('click', async function(event){
        event.preventDefault();
        console.log(this.dataset.href);
        let response=await fetch(this.dataset.href);
        let result= await response.json();
        console.log(result.template)
        modalContent.innerHTML=result.template
        wrapperModal.classList.add('modal__wrapper_visible')
        // определяем кнопку отмены удаления ... 
        let confirmationBtnNo= modalContent.querySelector('.confirmation__btn_no');
        confirmationBtnNo.addEventListener('click', (event)=>{
            // отменяем действие по умолчанию... просто закрываем модальное окно подтверждения
            event.preventDefault();
            wrapperModal.classList.remove('modal__wrapper_visible');
        })


    })
})
```
