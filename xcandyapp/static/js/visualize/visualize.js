/***** Line Chart *****/
let lineChart_vis = document.getElementById("lineChart_vis").getContext("2d");

// Global Options
Chart.defaults.global.defaultFontFamily = "Montserrat";
Chart.defaults.global.defaultFontSize = 17;
Chart.defaults.global.defaultFontColor = "#888";

let massPopChart = new Chart(lineChart_vis, {
  type: "line", // bar, horizontalBar, pie, line, doughnut, radar, polarArea
  data: {
    labels: [
      "7",
      "8",
      "9",
      "10",
      "11",
      "12",
      "13",
      "14",
      "15",
      "16",
      "17",
      "18",
      "19"
    ],
    datasets: [
      {
        label: "BG",
        data: [0, 110, 90, 140, 225, 60, 125, 220, 150, 160, 100, 80, 30, 20],
        backgroundColor: "#33333300",
        borderWidth: 2,
        borderColor: "#333333",
        hoverBorderWidth: 3,
        hoverBorderColor: "#333333"
      },
      {
        label: "BG Forecast",
        data: [0, 110, 90, 140, 225, 60, 125, 220, 150, 160, 100, 80, 30, 20],
        backgroundColor: "#74E4B100",
        borderWidth: 4,
        borderColor: "#25cb80",
        hoverBorderWidth: 5,
        hoverBorderColor: "#74E4B1"
      }
    ]
  },
  options: {
    title: {
      display: true,
      text: "",
      fontSize: 25
    },
    legend: {
      display: true,
      position: "bottom",
      labels: {
        fontColor: "#888"
      }
    },
    layout: {
      padding: {
        left: 2,
        right: 0,
        bottom: 0,
        top: 0
      }
    },
    tooltips: {
      enabled: true
    }
  }
});

/***** Bubble Chart *****/
var popCanvas_vis = document.getElementById("popChart_vis");

var popData = {
  datasets: [
    {
      label: [""],
      data: [
        {
          x: 7,
          y: 110,
          r: 14
        },
        {
          x: 8,
          y: 90,
          r: 14
        },
        {
          x: 9,
          y: 140,
          r: 14
        },
        {
          x: 10,
          y: 225,
          r: 14
        },
        {
          x: 11,
          y: 60,
          r: 14
        },
        {
          x: 12,
          y: 125,
          r: 14
        },
        {
          x: 13,
          y: 250,
          r: 14
        },
        {
          x: 14,
          y: 150,
          r: 14
        },
        {
          x: 15,
          y: 160,
          r: 14
        },
        {
          x: 16,
          y: 100,
          r: 14
        },
        {
          x: 17,
          y: 80,
          r: 14
        },
        {
          x: 18,
          y: 30,
          r: 14
        },
        {
          x: 19,
          y: 20,
          r: 14
        }
      ],
      backgroundColor: "#2d85c3ff",
      borderColor: "#2d85c3",
      borderWidth: 2,
      hoverBorderWidth: 3,
      radius: 10
    },
    {
      label: [""],
      data: [
        {
          x: 7,
          y: 110 - 50,
          r: 14
        },
        {
          x: 8,
          y: 90 - 50,
          r: 14
        },
        {
          x: 9,
          y: 140 - 50,
          r: 14
        },
        {
          x: 10,
          y: 225 - 50,
          r: 14
        },
        {
          x: 11,
          // y: 60 - 50,
          r: 14
        },
        {
          x: 12,
          y: 125 - 50,
          r: 14
        },
        {
          x: 13,
          y: 250 - 50,
          r: 14
        },
        {
          x: 14,
          y: 150 - 50,
          r: 14
        },
        {
          x: 15,
          y: 160 - 50,
          r: 14
        },
        {
          x: 16,
          y: 100 - 50,
          r: 14
        },
        {
          x: 17,
          y: 80 - 50,
          r: 14
        },
        {
          x: 18,
          // y: 30,
          r: 14
        },
        {
          x: 19,
          // y: 20,
          r: 14
        }
      ],
      backgroundColor: "#FBDF00ff",
      borderColor: "#FBDF00",
      borderWidth: 2,
      hoverBorderWidth: 3
    },
    {
      label: [""],
      data: [
        {
          x: 7,
          y: 110 - 100,
          r: 14
        },
        {
          x: 8,
          // y: 90 - 100,
          r: 14
        },
        {
          x: 9,
          y: 140 - 100,
          r: 14
        },
        {
          x: 10,
          y: 225 - 100,
          r: 14
        },
        {
          x: 11,
          // y: 60 - 100,
          r: 14
        },
        {
          x: 12,
          y: 125 - 100,
          r: 14
        },
        {
          x: 13,
          y: 250 - 100,
          r: 14
        },
        {
          x: 14,
          y: 150 - 100,
          r: 14
        },
        {
          x: 15,
          y: 160 - 100,
          r: 14
        },
        {
          x: 16,
          y: 100 - 100,
          r: 14
        },
        {
          x: 17,
          // y: 80 - 100,
          r: 14
        },
        {
          x: 18,
          // y: 30,
          r: 14
        },
        {
          x: 19,
          // y: 20,
          r: 14
        }
      ],
      backgroundColor: "#F5005Cff",
      borderColor: "#F5005C",
      borderWidth: 2,
      hoverBorderWidth: 3
    },
    {
      label: [""],
      data: [
        {
          x: 7,
          // y: 110 - 150,
          r: 14
        },
        {
          x: 8,
          // y: 90 - 150,
          r: 14
        },
        {
          x: 9,
          // y: 140 - 150,
          r: 14
        },
        {
          x: 10,
          y: 225 - 150,
          r: 14
        },
        {
          x: 11,
          // y: 60 - 150,
          r: 14
        },
        {
          x: 12,
          // y: 125 - 150,
          r: 14
        },
        {
          x: 13,
          y: 250 - 150,
          r: 14
        },
        {
          x: 14,
          y: 150 - 150,
          r: 14
        },
        {
          x: 15,
          y: 160 - 150,
          r: 14
        },
        {
          x: 16,
          // y: 100 - 150,
          r: 14
        },
        {
          x: 17,
          // y: 80 - 150,
          r: 14
        },
        {
          x: 18,
          // y: 30,
          r: 14
        },
        {
          x: 19,
          // y: 20,
          r: 14
        }
      ],
      backgroundColor: "#25cb80ff",
      borderColor: "#25cb80",
      borderWidth: 2,
      hoverBorderWidth: 3
    }
  ]
};

var bubbleChart = new Chart(popCanvas_vis, {
  type: "bubble",
  data: popData
});