import "./Login.css";

import { useState } from "react";

import { useNavigate } from "react-router-dom";

import axios from "axios";

import {

    MdSecurity,

    MdEmail,

    MdLock,

    MdArrowForward

} from "react-icons/md";

function Login(){

    const navigate = useNavigate();

    const [email,setEmail] = useState("");

    const [password,setPassword] = useState("");

    const [loading,setLoading] = useState(false);

    const [error,setError] = useState("");

    const handleLogin = async () => {

        setLoading(true);

        setError("");

        try{

            const response = await axios.post(

                "http://127.0.0.1:8000/auth/login",

                {

                    email,

                    password

                }

            );

            localStorage.setItem(

                "token",

                response.data.access_token

            );

            navigate("/dashboard");

        }

        catch(err){

            if(err.response){

                setError(

                    err.response.data.detail

                );

            }

            else{

                setError(

                    "Unable to connect to QuantumShield-X Server."

                );

            }

        }

        finally{

            setLoading(false);

        }

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

                        Analyze vulnerable cryptographic algorithms, receive AI-powered migration recommendations and secure enterprise applications against future quantum attacks.

                    </p>

                </div>

                <div className="feature-list">

                    <div className="feature-item">

                        <MdSecurity/>

                        <span>

                            Quantum Risk Detection

                        </span>

                    </div>

                    <div className="feature-item">

                        <MdSecurity/>

                        <span>

                            AI Migration Recommendations

                        </span>

                    </div>

                    <div className="feature-item">

                        <MdSecurity/>

                        <span>

                            PQC Readiness Assessment

                        </span>

                    </div>

                    <div className="feature-item">

                        <MdSecurity/>

                        <span>

                            Enterprise Security Dashboard

                        </span>

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

                            value={email}

                            onChange={(e)=>setEmail(e.target.value)}

                            autoComplete="email"

                        />

                    </div>

                    <div className="input-group">

                        <MdLock className="input-icon"/>

                        <input

                            type="password"

                            placeholder="Password"

                            value={password}

                            onChange={(e)=>setPassword(e.target.value)}

                            autoComplete="current-password"

                        />

                    </div>

                    {

                        error && (

                            <p className="login-error">

                                {error}

                            </p>

                        )

                    }

                    <div className="login-options">

                        <label>

                            <input

                                type="checkbox"

                            />

                            Remember Me

                        </label>

                        <a href="#">

                            Forgot Password?

                        </a>

                    </div>

                    <button

                        className="login-btn"

                        onClick={handleLogin}

                        disabled={loading}

                    >

                        {

                            loading

                            ?

                            "Signing In..."

                            :

                            <>

                                Sign In

                                <MdArrowForward/>

                            </>

                        }

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