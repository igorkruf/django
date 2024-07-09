https://www.npmjs.com/package/js-datepicker   - npmjs.com

```
console.log('подключили custom.js');
let picker = datepicker('.datepicker1', {id:1, onSelect:(instance, date)=>{
    console.log('выбрали дату');
    let dateManday=getMonday(date)
    console.log(`Дата понедельника: ${dateManday}`);
    let dateSunday=getSunday(date)
    console.log(`Дата воскресенья: ${dateSunday}`);
}, startDay: 1, showAllDates: true,  });

function getMonday(d) {
    d = new Date(d);
    var day = d.getDay(),
      diff = d.getDate() - day + (day == 0 ? -6 : 1); // adjust when day is sunday
    return new Date(d.setDate(diff));
  }

  function getSunday(d) {
    d = new Date(d);
    var day = d.getDay(),
      diff = d.getDate()-day + (day == 0 ? 0 : 7); // adjust when day is sunday
    return new Date(d.setDate(diff));
  }

```
