import "./Navbar.css";
import { useNavigate } from "react-router-dom";

function Navbar() {

    const navigate = useNavigate();

    const logout = () => {

        localStorage.removeItem("access_token");

        navigate("/");

    };

    return (

        <nav className="navbar">

            <div className="logo">
                🛡 QuantumShield-X
            </div>

            <div className="user-section">

                <span className="user">
                    👤 Demo User
                </span>

                <button
                    className="logout-btn"
                    onClick={logout}
                >
                    Logout
                </button>

            </div>

        </nav>

    );

}

export default Navbar;