```
option = {
  legend: {
   
    orient: 'horizontal',
    right: 10,
    
  },
  
  xAxis: {
    show:true,
    type: 'category',
    axisTick:{
      show:true,
  
    },
    boundaryGap: false,
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {
    show:true,
    position :'right',
    axisLine:{
      show:true,
    },
    axisTick:{
      show:true,
 
    },
  },
  series: [
    {
      color:'red',
      lineStyle:{
        color:'red',
        
      },
      areaStyle:{
        color:'red',
        opacity:0.2,
        
      },
      name:'Август',
      colorBy:'series',
      symbol:'emptyCircle',
      data: [820, 932, 901, 934, 1290, 1330, 1320],
      type: 'line',
      markLine:{
        silent:true,
      },
      // areaStyle: {}
    }
  ]
};
```
#########################################################################################
```
console.log('Подключили js ')
var chartDom = document.querySelector('.home');
var myChart = echarts.init(chartDom);
var option= {
  xAxis: {
    type: 'category',
    boundaryGap: false,
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      data: [820, 932, 901, 934, 1290, 1330, 1320],
      type: 'line',
      areaStyle: {}
    },
    
  ]
};
let cloneOption = structuredClone(option);
// Моё ////////////////////////////
let btnAddSeries = document.querySelector('.add-series');
let arr=[{
    data: [520, 332, 501, 534, 990, 1030, 1120],
    type: 'line',
    areaStyle: {}
  },
  {
    data: [250, 352, 521, 554, 990, 1050, 1170],
    type: 'line',
    areaStyle: {}
  }];


btnAddSeries.addEventListener('click', ()=>{
  cloneOption=structuredClone(option)
  console.log(cloneOption)
arr.forEach((elem)=>{
  cloneOption['series'].push(elem);
})
//   option['series'].{
//     id:1,
//     data: [220, 332, 501, 534, 990, 1030, 1120],
//     type: 'line',
//     areaStyle: {}
//   },
//   {
//     id:1,
//     data: [250, 352, 521, 554, 990, 1050, 1170],
//     type: 'line',
//     areaStyle: {}
//   }]
// );
   myChart.setOption(cloneOption);
})
// /////////////////////////////////////


option && myChart.setOption(option);

```
