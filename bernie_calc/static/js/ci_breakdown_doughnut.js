let ci_data_obj = JSON.parse(document.getElementById('ci-income-doughnut-data').textContent);
let ci_data = []
let ci_labels = []

$(document).ready(function() {

  ci_data.push(ci_data_obj.monthly_healthcare_spending);
  ci_labels.push('Healthcare Spending');

  ci_data.push(ci_data_obj.monthly_taxes);
  ci_labels.push('Taxes');

  ci_data.push(ci_data_obj.monthly_income);
  ci_labels.push('Income');

  if (ci_data_obj.student_loans > 0){
    ci_data.push(ci_data_obj.student_loans);
    ci_labels.push('Student Loans');
  }

  if(ci_data_obj.medical_debt > 0 ){
    ci_data.push(ci_data_obj.medical_debt);
    ci_labels.push('Medical Debt');
  }
  
  var config = {
    type: 'pie',
    data: {
      datasets: [{
        data: ci_data,
        backgroundColor: [
          "#1EF5CC",
          "#f51e47",
          "#2b9cd9",
          "#949FB1",
          "#4D5360",
        ],
        label: 'Dataset 1'
      }],
      labels: ci_labels
    },
    options: {
      responsive: true,
      maintainAspectRatio : false,
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Your current income breakdown'
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
  
  var ctx2 = document.getElementById("ciDoughnutChart").getContext("2d");
  new Chart(ctx2, config);
  

});