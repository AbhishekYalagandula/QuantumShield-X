import "./Login.css";
import { useNavigate } from "react-router-dom";

function Login() {
    const navigate = useNavigate();
  return (
    <div className="login-page">
      <div className="login-card">

        <h1 className="title">QuantumShield-X</h1>

        <p className="subtitle">
          Quantum Security. Future Ready.
        </p>

        <h2>Welcome Back!</h2>

        <input
          type="email"
          placeholder="Email Address"
        />

        <input
          type="password"
          placeholder="Password"
        />

        <button
    onClick={() => navigate("/dashboard")}
>
    LOGIN
</button>
      </div>
    </div>
  );
}

export default Login;