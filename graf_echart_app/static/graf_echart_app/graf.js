let barGraf= (container_selector, dataX, dataY)=>{

    var myChart = echarts.init(document.querySelector(container_selector));
    window.addEventListener('resize', function() {
      
      myChart.resize();
    });

        // Specify the configuration items and data for the chart
        var option = {
          title: {
            text: 'Столбчатая диаграмма'
          },
          tooltip: {},
          legend: {
            
          },
          toolbox:{
            show:true,
            itemSize:15,
            feature:{
              saveAsImage:{
                type:'png',
                
              }

            }


          },
          grid:{
            show:false,
          },
          xAxis: {
            data: dataX,
          },
          yAxis: {},
          series: [
            {
              type: 'line',
              smooth: true,
              data: dataY
            }
          ]
        };
  
        // Display the chart using the configuration items and data just specified.
        myChart.setOption(option);
        return myChart;
}

let lineGraf=(containerSelector, sources)=>{
  let myChart = echarts.init(document.querySelector(containerSelector));
  window.addEventListener('resize', function() {
   myChart.resize();
  });
  console.log(sources);
  let option={
    // tooltip: {
    //   alwaysShowContent: true,
    //   trigger: 'axis',
    //   // alwaysShowContent: false ,
    //   axisPointer: { 
        
    //     type: 'cross'
    //    }
    // },
    
    legend: {},
    dataset:{
      source:sources
    },
    xAxis:{
      
      type:'category',
     
    },
    yAxis:{
      
    },
    series: [
      { type: 'line', seriesLayoutBy: 'row' },
      { type: 'line', seriesLayoutBy: 'row' },
      { type: 'line', seriesLayoutBy: 'row' },
    ], 

  };
  myChart.setOption(option);
  return myChart;
}