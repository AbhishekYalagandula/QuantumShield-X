import "./RiskAnalyzer.css";

import Navbar from "../components/Navbar/Navbar";

import {

    MdAnalytics,

    MdWarning,

    MdCheckCircle,

    MdTrendingUp,

    MdSecurity

} from "react-icons/md";

function RiskAnalyzer(){

    return(

        <>

            <Navbar/>

            <main className="risk-page">

                <section className="risk-header">

                    <h1>

                        Quantum Risk Analyzer

                    </h1>

                    <p>

                        AI-powered analysis of cryptographic vulnerabilities and post-quantum readiness.

                    </p>

                </section>

                <section className="risk-card">

                    <div className="risk-top">

                        <div className="risk-icon">

                            <MdAnalytics/>

                        </div>

                        <div>

                            <h2>

                                Overall Quantum Risk

                            </h2>

                            <p>

                                QuantumShield-X combines AI analysis with cryptographic assessment to determine migration priority.

                            </p>

                        </div>

                    </div>

                    <div className="risk-score-card">

                        <div className="risk-score">

                            <h1>

                                74%

                            </h1>

                            <span>

                                Medium Risk

                            </span>

                        </div>

                        <div className="risk-progress">

                            <div className="progress-bar">

                                <div

                                    className="progress-fill"

                                    style={{

                                        width:"74%"

                                    }}

                                >

                                </div>

                            </div>

                        </div>

                    </div>

                    <div className="risk-grid">

                        <div className="risk-item">

                            <MdWarning className="risk-item-icon warning"/>

                            <div>

                                <h3>

                                    Critical Risks

                                </h3>

                                <p>

                                    8 Vulnerabilities

                                </p>

                            </div>

                        </div>

                        <div className="risk-item">

                            <MdTrendingUp className="risk-item-icon"/>

                            <div>

                                <h3>

                                    Migration Priority

                                </h3>

                                <p>

                                    High

                                </p>

                            </div>

                        </div>
                                                <div className="risk-item">

                            <MdCheckCircle className="risk-item-icon success"/>

                            <div>

                                <h3>

                                    Safe Algorithms

                                </h3>

                                <p>

                                    15 Verified

                                </p>

                            </div>

                        </div>

                        <div className="risk-item">

                            <MdSecurity className="risk-item-icon"/>

                            <div>

                                <h3>

                                    PQC Readiness

                                </h3>

                                <p>

                                    61%

                                </p>

                            </div>

                        </div>

                    </div>

                    <div className="analysis-card">

                        <h2>

                            AI Risk Analysis

                        </h2>

                        <p>

                            QuantumShield-X detected multiple RSA and ECC implementations that are vulnerable to future quantum attacks using Shor's Algorithm. Immediate migration to ML-KEM (CRYSTALS-Kyber) and ML-DSA (Dilithium) is recommended for long-term security.

                        </p>

                    </div>

                    <div className="risk-summary">

                        <div className="summary-box">

                            <h3>

                                Vulnerable Algorithms

                            </h3>

                            <h1>

                                12

                            </h1>

                        </div>

                        <div className="summary-box">

                            <h3>

                                AI Confidence

                            </h3>

                            <h1>

                                98%

                            </h1>

                        </div>

                        <div className="summary-box">

                            <h3>

                                Overall Status

                            </h3>

                            <h1>

                                Medium

                            </h1>

                        </div>

                    </div>

                </section>

            </main>

        </>

    );

}

export default RiskAnalyzer;