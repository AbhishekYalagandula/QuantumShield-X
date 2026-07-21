import "./Login.css";

import { useNavigate } from "react-router-dom";

import {

    MdSecurity,

    MdEmail,

    MdLock,

    MdArrowForward

} from "react-icons/md";

function Login(){

    const navigate = useNavigate();

    const handleLogin = () => {

        navigate("/dashboard");

    };

    return(

        <div className="login-page">
                        <div className="login-left">

                <div className="brand">

                    <div className="brand-logo">

                        <MdSecurity/>

                    </div>

                    <h1>

                        QuantumShield-X

                    </h1>

                    <p>

                        Post-Quantum Cryptography Migration Toolkit

                    </p>

                </div>

                <div className="hero-content">

                    <h2>

                        Protect Today's Data Against Tomorrow's Quantum Threats

                    </h2>

                    <p>

                        Analyze vulnerable cryptographic algorithms, receive AI-powered migration recommendations, and secure your applications with post-quantum cryptography.

                    </p>

                </div>

                <div className="feature-list">

                    <div className="feature-item">

                        <MdSecurity/>

                        <span>Quantum Risk Detection</span>

                    </div>

                    <div className="feature-item">

                        <MdSecurity/>

                        <span>AI Migration Recommendations</span>

                    </div>

                    <div className="feature-item">

                        <MdSecurity/>

                        <span>PQC Readiness Assessment</span>

                    </div>

                    <div className="feature-item">

                        <MdSecurity/>

                        <span>Enterprise Security Dashboard</span>

                    </div>

                </div>

            </div>

            <div className="login-right">

                <div className="login-card">

                    <h2>

                        Welcome Back

                    </h2>

                    <p>

                        Sign in to continue to QuantumShield-X

                    </p>
                                        <div className="input-group">

                        <MdEmail className="input-icon"/>

                        <input

                            type="email"

                            placeholder="Email Address"

                        />

                    </div>

                    <div className="input-group">

                        <MdLock className="input-icon"/>

                        <input

                            type="password"

                            placeholder="Password"

                        />

                    </div>

                    <div className="login-options">

                        <label>

                            <input type="checkbox"/>

                            Remember Me

                        </label>

                        <a href="#">

                            Forgot Password?

                        </a>

                    </div>

                    <button

                        className="login-btn"

                        onClick={handleLogin}

                    >

                        Sign In

                        <MdArrowForward/>

                    </button>

                    <div className="login-footer">

                        <p>

                            Team Amaravati Qubits

                        </p>

                        <span>

                            QuantumShield-X v1.0

                        </span>

                    </div>

                </div>

            </div>

        </div>

    );

}

export default Login;