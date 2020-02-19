let bi_data_obj = JSON.parse(document.getElementById('bi-income-doughnut-data').textContent);
let bi_data = []
let bi_labels = []

$(document).ready(function() {

  bi_data.push(bi_data_obj.monthly_taxes);
  bi_labels.push('Taxes');

  bi_data.push(bi_data_obj.monthly_income);
  bi_labels.push('Income');

  
  var config = {
    type: 'pie',
    data: {
      datasets: [{
        data: bi_data,
        backgroundColor: [
          "#f51e47",
          "#2b9cd9",
        ],
        label: 'Dataset 1'
      }],
      labels: bi_labels
    },
    options: {
      responsive: true,
      maintainAspectRatio : false,
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Income breakdown under Bernie'
      },
      animation: {
        animateScale: true,
        animateRotate: true
      },
      tooltips: {
        callbacks: {
          label:
          function(tooltipItem, data){
            var tooltip_index = tooltipItem.index;
            return  '$' + data.datasets[0].data[tooltip_index].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
          }
        }
      }
    }
  };
  
  var ctx2 = document.getElementById("biDoughnutChart").getContext("2d");
  new Chart(ctx2, config);
  

});