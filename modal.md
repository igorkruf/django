base.html
```
 <div class="modal__wrapper  modal__wrapper_visible ">
        <div class="modal">
            <div class="modal__header">
                <div class="modal__title">Заголовок модалки</div>
                <div class="modal__close">Зарыть</div>
            </div>
            <div class="modal__content">
                content 
                <span class="open-sub-modal">Открыть подмодалку</span>
            </div>
        </div>
    </div>
    <template id="template-sub-modal">
        <div class="modal__wrapper modal__wrapper_visible sub-modal__wrapper">
            <div class="modal sub-modal">
                <div class="modal__header ">
                    <div class="modal__title">Заголовок под модалки</div>
                    <div class="modal__close ">Зарыть под модалку</div>
                </div>
                <div class="modal__content sub-modal__content">
                    content под модалки
                </div>
            </div>
        </div>
    </template>
```
js
```
let tagTemplateSubModal=document.querySelector('#template-sub-modal');
let modalWrapper=document.querySelector('.modal__wrapper');
let templateSubModal=tagTemplateSubModal.content.cloneNode(true);
let spanOpenSubModal=modalWrapper.querySelector('.open-sub-modal');

spanOpenSubModal.addEventListener('click', ()=>{
    console.log('ddddddddddddddddd');
    modalWrapper.append(templateSubModal);
    let subModalWrapper=document.querySelector('.sub-modal__wrapper');
    subModalWrapper.classList.add('modal__wrapper_visible');
    let subModalClose= subModalWrapper.querySelector('.modal__close');
        subModalWrapper.addEventListener('click', (event)=>{
            event.stopPropagation();
            if ((event.target == subModalWrapper) || (event.target == subModalClose)) {
                subModalWrapper.classList.remove('modal__wrapper_visible');
            };
           
        })
})
```
css
```
.modal{
    background-color: #fff;
    width:90%;
    max-width:600px;
}

.modal__wrapper{
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:100vh;
    background-color: rgba(0, 0, 0, 0.249);
    display:flex;
    justify-content: center;
    align-items: center;
    visibility: hidden;
    opacity:0;
    transition:all 1S linear;
    
}

.modal__wrapper_visible{
    visibility: visible;
    opacity:1;
}

.modal__header{
    display:flex;
    justify-content: space-between;
}

.modal__close{
    cursor:pointer;
}

.open-sub-modal{
    cursor:pointer;
    color:blue;
}
```
