import "./Sidebar.css";
import { useNavigate, useLocation } from "react-router-dom";

function Sidebar() {

    const navigate = useNavigate();
    const location = useLocation();

    const logout = () => {
        localStorage.removeItem("access_token");
        navigate("/");
    };

    return (

        <div className="sidebar">

            <div className="sidebar-logo">
                🛡
                <h2>QuantumShield-X</h2>
            </div>

            <div className="sidebar-menu">

                <button
                    className={location.pathname === "/dashboard" ? "active" : ""}
                    onClick={() => navigate("/dashboard")}
                >
                    🏠 Dashboard
                </button>

                <button
                    className={location.pathname === "/upload" ? "active" : ""}
                    onClick={() => navigate("/upload")}
                >
                    📤 Upload Project
                </button>

                <button
                    className={location.pathname === "/scanner" ? "active" : ""}
                    onClick={() => navigate("/scanner")}
                >
                    🔍 Code Scanner
                </button>

                <button
                    className={location.pathname === "/certificate" ? "active" : ""}
                    onClick={() => navigate("/certificate")}
                >
                    📜 Certificate Scanner
                </button>

                <button
                    className={location.pathname === "/risk" ? "active" : ""}
                    onClick={() => navigate("/risk")}
                >
                    ⚠ Risk Analyzer
                </button>

                <button
                    className={location.pathname === "/recommendation" ? "active" : ""}
                    onClick={() => navigate("/recommendation")}
                >
                    🤖 AI Recommendation
                </button>

                <button
                    className={location.pathname === "/migration" ? "active" : ""}
                    onClick={() => navigate("/migration")}
                >
                    📈 Migration Planner
                </button>

                <button
                    className={location.pathname === "/report" ? "active" : ""}
                    onClick={() => navigate("/report")}
                >
                    📄 Reports
                </button>

                <button
                    className={location.pathname === "/settings" ? "active" : ""}
                    onClick={() => navigate("/settings")}
                >
                    ⚙ Settings
                </button>

            </div>

            <div className="sidebar-bottom">

                <button
                    className="logout-btn"
                    onClick={logout}
                >
                    🚪 Logout
                </button>

            </div>

        </div>

    );
}

export default Sidebar;