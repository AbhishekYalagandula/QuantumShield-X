import "./RiskTrend.css";
import {
  ResponsiveContainer,
  AreaChart,
  Area,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
} from "recharts";

const riskData = [
  { month: "Jan", risk: 82 },
  { month: "Feb", risk: 76 },
  { month: "Mar", risk: 70 },
  { month: "Apr", risk: 67 },
  { month: "May", risk: 61 },
  { month: "Jun", risk: 55 },
];

function RiskTrend() {
  return (
    <div className="risk-trend-card">
      <div className="trend-header">
        <div>
          <h2>Quantum Risk Trend</h2>
          <p>Overall organizational security improvement</p>
        </div>

        <button className="trend-btn">
          Last 6 Months
        </button>
      </div>

      <div className="trend-chart">
        <ResponsiveContainer width="100%" height={300}>
          <AreaChart data={riskData}>
            <defs>
              <linearGradient
                id="riskGradient"
                x1="0"
                y1="0"
                x2="0"
                y2="1"
              >
                <stop
                  offset="0%"
                  stopColor="#6C63FF"
                  stopOpacity={0.5}
                />
                <stop
                  offset="100%"
                  stopColor="#6C63FF"
                  stopOpacity={0}
                />
              </linearGradient>
            </defs>

            <CartesianGrid
              strokeDasharray="4 4"
              stroke="#23385e"
            />

            <XAxis
              dataKey="month"
              stroke="#8fa4d3"
            />

            <YAxis
              stroke="#8fa4d3"
              domain={[0, 100]}
            />

            <Tooltip
              contentStyle={{
                background: "#12203d",
                border: "1px solid #2e4b7f",
                borderRadius: "12px",
                color: "#ffffff",
              }}
            />

            <Area
              type="monotone"
              dataKey="risk"
              stroke="#6C63FF"
              strokeWidth={4}
              fill="url(#riskGradient)"
            />

            <Line
              type="monotone"
              dataKey="risk"
              stroke="#3B82F6"
              strokeWidth={3}
              dot={{
                r: 5,
                fill: "#3B82F6",
              }}
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>

      <div className="trend-footer">
        <div className="trend-stat">
          <h3>55%</h3>
          <span>Current Risk</span>
        </div>

        <div className="trend-stat">
          <h3>-27%</h3>
          <span>Improvement</span>
        </div>

        <div className="trend-stat">
          <h3>6</h3>
          <span>Assessments</span>
        </div>
      </div>
    </div>
  );
}

export default RiskTrend;