import "./QuickActions.css";
import { useNavigate } from "react-router-dom";

function QuickActions() {
  const navigate = useNavigate();
  return (
    <div className="actions-box">

      <h2>⚡ Quick Actions</h2>

     <button
    className="action-btn upload"
    onClick={() => navigate("/upload")}
>
    📤 Upload Project
</button>

      <button className="action-btn scan">
        🛡 Start Quantum Scan
      </button>

      <button className="action-btn report">
        📄 Generate Report
      </button>

      <button className="action-btn download">
        ⬇ Download Report
      </button>

    </div>
  );
}

export default QuickActions;