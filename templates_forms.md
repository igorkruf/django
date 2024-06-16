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
