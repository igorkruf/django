https://habr.com/ru/companies/ruvds/articles/445276/   - useEffect

https://doka.guide/js/intersection-observer/?ysclid=m36yg23sxf187984357  - про intersectionObserver

https://utyatnishna.ru/info/132044/can-i-use-socketio-with-django   как подружить socket io и django  

https://penpot.app/design  - бесплатный аналог figma

https://stackoverflow.com/questions/51452593/how-to-add-react-components-to-existing-django-project     - встроить в приложение django React


https://github.com/protibimbok/django-vite-plugin?ysclid=m5e3h5akru226851176    - vite.config   с django

https://gist.github.com/lucianoratamero/7fc9737d24229ea9219f0987272896a2?permalink_comment_id=4464562 - ещё


https://www.techiediaries.com/django-cors/  - про CORS и DRF

https://reactrouter.docschina.org/routers/create-browser-router/  реакт роутер

https://blog.logrocket.com/using-react-intersection-observer-create-dynamic-header/  -intersectionObserver 

```

function App() {
 
useEffect(()=>{
  let listBlocks = document.querySelectorAll('.block');
  let options = {
       threshold:[0]
      };
  let callback = (entries)=>{
    entries.forEach(entry => {
    if (entry.isIntersecting){
            console.log('есть вхождение');
            observer.unobserve(entry.target);
     }
        });  
     };
        
  let observer = new IntersectionObserver(callback, options);
  listBlocks.forEach((block)=>{observer.observe(block);});

},[]) 
//  let options = {
//   threshold:[0]
//  }

//  let callback = (entries)=>{
//   entries.forEach(entry => {
//     if (entry.isIntersecting){
//       console.log(entry);
//     }
    
//   });

//  };
//  let observer = new IntersectionObserver(callback, options);


//  let listBlocks = document.querySelectorAll('.block');
//  listBlocks.forEach((block)=>{
//   observer.observe(block);
//  })

 
  return <>
    
    <div className="block__wrapper">
      <div className="block">1</div>              
      <div className="block">2</div>
      <div className="block">3</div>
      <div className="block">4</div>              
      <div className="block">5</div>
      <div className="block">6</div>                            
    </div>
    
  
    
    
    </>
    
    
};

export default App
```



