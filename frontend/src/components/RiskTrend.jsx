import "./RiskTrend.css";

import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

import { Line } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const data = {
  labels: ["Apr", "May", "Jun", "Jul", "Aug", "Sep"],
  datasets: [
    {
      label: "Risk Score",
      data: [42, 51, 56, 61, 68, 72],
      borderColor: "#6f6cff",
      backgroundColor: "rgba(111,108,255,0.2)",
      borderWidth: 4,
      tension: 0.4,
      fill: true,
      pointBackgroundColor: "#6f6cff",
      pointRadius: 5,
      pointHoverRadius: 8,
    },
  ],
};

const options = {
  responsive: true,

  plugins: {
    legend: {
      display: false,
    },
  },

  scales: {
    x: {
      ticks: {
        color: "#ffffff",
      },
      grid: {
        color: "rgba(14, 14, 14, 0.9)",
      },
    },

    y: {
      min: 30,
      max: 80,

      ticks: {
        color: "#ffffff",
      },

      grid: {
        color: "rgba(7, 7, 7, 0.98)",
      },
    },
  },
};

function RiskTrend() {
  return (
    <div className="trend-box">
      <h2>Risk Trend</h2>

      <Line data={data} options={options} />
    </div>
  );
}

export default RiskTrend;