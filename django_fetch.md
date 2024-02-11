////////////////////////////////////////////////////////////////////////
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
//////////////////////////////////////////////////////////////////////////
btnSave.addEventListener('click', async()=>{
            console.log(input.value)
            let formData=new FormData();
            formData.append("kolvo", input.value);
            let response= await fetch(`${btnSave.dataset.idsettype}/edit/`,{
                method:"POST",
                body:formData,
                headers: {
                  'X-CSRFToken': csrftoken,
                },
  });
  /////////////////////////////////////////////////////////////////////////

  let listBtn=document.querySelectorAll('.btn');
listBtn.forEach((elem)=>{
    elem.addEventListener('click', function(){

        let kolVoPart= this.previousElementSibling;
        let kolVo= kolVoPart.innerHTML;
        let parent=this.parentElement;
        let input=document.createElement('input');
        input.className="input__kolvo";
        input.type="number";
        input.min=1;
        input.value=kolVo;
        input.addEventListener('input', (e)=>{
            let regExp=/\d+$/g;
            if (!regExp.test(e.target.value)){
                console.log('Вводим нечисло!!!')
                    input.nextElementSibling.nextElementSibling.classList.remove('btn__save_visible')
            } else {
                if (e.target.value>0){
                input.nextElementSibling.nextElementSibling.classList.add('btn__save_visible')
            }
            }

        })
        parent.replaceChild(input,kolVoPart);
        this.style.display="none";
        console.log(this)
        let btnSave=this.nextElementSibling;
        console.log(btnSave);
        btnSave.addEventListener('click', async()=>{
            console.log(input.value)
            let formData=new FormData();
            formData.append("kolvo", input.value);
            let response= await fetch(`${btnSave.dataset.idsettype}/edit/`,{
                method:"POST",
                body:formData,
                headers: {
                            
                    'X-CSRFToken': csrftoken,
            },
            });
        })
    })
})

<div class="wrap"><div>{{item_settype_by_type.part.name}}</div>-<div class="kolvo-part">{{item_settype_by_type.kol_vo}}</div><button class="btn" ">Редактировать</button><button class="btn__save"  data-idsettype="3">Сохранить</button></div>
