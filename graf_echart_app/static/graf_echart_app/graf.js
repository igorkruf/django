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

let lineGraf=(containerSelector, dataX, listDataY)=>{
  let myChart = echarts.init(document.querySelector(containerSelector));
  window.addEventListener('resize', function() {
   myChart.resize();
  });

  let option={
    xAxis:{
      type:'category',
      data:dataX
    },
    yAxis:{},
    series: listDataY, 
  };
  myChart.setOption(option);
  return myChart;
}