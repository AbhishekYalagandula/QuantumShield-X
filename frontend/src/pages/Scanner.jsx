import "./Scanner.css";

import { useState } from "react";

import Navbar from "../components/Navbar/Navbar";

import {

    MdSecurity,

    MdCheckCircle,

    MdWarning,

    MdRefresh,

    MdAnalytics

} from "react-icons/md";

function Scanner(){

    const [scanning,setScanning]=useState(true);

    const [progress,setProgress]=useState(68);

    return(

        <>

            <Navbar/>

            <main className="scanner-page">

                <section className="scanner-header">

                    <h1>

                        Quantum Security Scanner

                    </h1>

                    <p>

                        Scanning uploaded project for vulnerable cryptographic algorithms

                    </p>

                </section>

                <section className="scanner-card">

                    <div className="scan-status">

                        <div className="scan-icon">

                            <MdRefresh/>

                        </div>

                        <div>

                            <h2>

                                Scan In Progress

                            </h2>

                            <p>

                                AI Engine + Qiskit Analyzer

                            </p>

                        </div>

                    </div>

                    <div className="progress-section">

                        <div className="progress-header">

                            <span>

                                Overall Progress

                            </span>

                            <strong>

                                {progress}%

                            </strong>

                        </div>

                        <div className="progress-bar">

                            <div

                                className="progress-fill"

                                style={{

                                    width:`${progress}%`

                                }}

                            >

                            </div>

                        </div>

                    </div>
                                        <div className="scan-results">

                        <div className="result-card">

                            <MdWarning className="result-icon warning"/>

                            <div>

                                <h3>

                                    RSA-2048 Detected

                                </h3>

                                <p>

                                    High Quantum Risk

                                </p>

                            </div>

                        </div>

                        <div className="result-card">

                            <MdWarning className="result-icon warning"/>

                            <div>

                                <h3>

                                    ECC Detected

                                </h3>

                                <p>

                                    Medium Quantum Risk

                                </p>

                            </div>

                        </div>

                        <div className="result-card">

                            <MdCheckCircle className="result-icon success"/>

                            <div>

                                <h3>

                                    AES-256

                                </h3>

                                <p>

                                    Quantum Safe (Recommended)

                                </p>

                            </div>

                        </div>

                    </div>

                    <div className="scanner-stats">

                        <div className="stat-box">

                            <MdSecurity/>

                            <h2>

                                12

                            </h2>

                            <span>

                                Vulnerable Algorithms

                            </span>

                        </div>

                        <div className="stat-box">

                            <MdAnalytics/>

                            <h2>

                                74%

                            </h2>

                            <span>

                                PQC Readiness

                            </span>

                        </div>

                        <div className="stat-box">

                            <MdCheckCircle/>

                            <h2>

                                5

                            </h2>

                            <span>

                                Safe Algorithms

                            </span>

                        </div>

                    </div>

                </section>

            </main>

        </>

    );

}

export default Scanner;