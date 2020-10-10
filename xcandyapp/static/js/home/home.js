/***** Bubble Chart *****/
var popCanvas_vis = document.getElementById("popChart_vis");

Chart.defaults.global.defaultFontFamily = "Montserrat";
Chart.defaults.global.defaultFontSize = 10;
Chart.defaults.global.defaultFontColor = "#555";
Chart.defaults.scale.gridLines.display = false;

var popData = {
  datasets: [{
      label: ["BG 1"],
      data: [{
          x: 7,
          y: 110,
          r: 5
        },
        {
          x: 8,
          y: 90,
          r: 5
        },
        {
          x: 9,
          y: 140,
          r: 5
        },
        {
          x: 10,
          y: 225,
          r: 5
        },
        {
          x: 11,
          y: 60,
          r: 5
        },
        {
          x: 12,
          y: 125,
          r: 5
        }
      ],
      radius: 2,
      backgroundColor: "#2d85c3",
      borderColor: "#2d85c3",
      borderWidth: 1
    },
    {
      label: ["BG 2"],
      data: [{
          x: 7,
          y: 110 - 50,
          r: 5
        },
        {
          x: 8,
          y: 90 - 50,
          r: 5
        },
        {
          x: 9,
          y: 140 - 50,
          r: 5
        },
        {
          x: 10,
          y: 225 - 50,
          r: 5
        },
        {
          x: 11,
          // y: 60 - 50,
          r: 5
        },
        {
          x: 12,
          y: 125 - 50,
          r: 5
        }
      ],
      backgroundColor: "#FBDF00",
      borderColor: "#FBDF00",
      borderWidth: 1
    },
    {
      label: ["BG 3"],
      data: [{
          x: 7,
          y: 110 - 100,
          r: 5
        },
        {
          x: 8,
          // y: 90 - 100,
          r: 5
        },
        {
          x: 9,
          y: 140 - 100,
          r: 5
        },
        {
          x: 10,
          y: 225 - 100,
          r: 5
        },
        {
          x: 11,
          // y: 60 - 100,
          r: 5
        },
        {
          x: 12,
          y: 125 - 100,
          r: 5
        }
      ],
      backgroundColor: "#F5005C",
      borderColor: "#F5005C",
      borderWidth: 1
    },
    {
      label: ["BG 4"],
      data: [{
          x: 7,
          // y: 110 - 150,
          r: 5
        },
        {
          x: 8,
          // y: 90 - 150,
          r: 5
        },
        {
          x: 9,
          // y: 140 - 150,
          r: 5
        },
        {
          x: 10,
          y: 225 - 150,
          r: 5
        },
        {
          x: 11,
          // y: 60 - 150,
          r: 5
        },
        {
          x: 12,
          // y: 125 - 150,
          r: 5
        }
      ],
      backgroundColor: "#25cb80",
      borderColor: "#25cb80",
      borderWidth: 1
    }
  ]
};

var bubbleChart = new Chart(popCanvas_vis, {
  type: "bubble",
  data: popData,
  options: {
    legend: {
      display: false
    },
    scales: {
      xAxes: [{
        gridLines: {
          display: false,
          drawBorder: false
        }
      }],
      yAxes: [{
        display: false,
        gridLines: {
          drawBorder: false
        }
      }]
    }
  }
});

$('#period').click(function () {
  if (this.checked) {
    period = 7;
  } else {
    period = 1;
  }
  $.ajax({
    url: '/home/glucose/',
    data: {
      'period': period
    },
    success: function (data) {
      alert('success');
      $('#avg_glucose').load(' #avg_glucose');
    }
  });
});