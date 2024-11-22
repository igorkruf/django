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
