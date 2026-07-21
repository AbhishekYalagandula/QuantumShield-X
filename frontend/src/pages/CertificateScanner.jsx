import "./CertificateScanner.css";

import Navbar from "../components/Navbar/Navbar";

import {

    MdVerifiedUser,

    MdSecurity,

    MdWarning,

    MdFingerprint,

    MdLock

} from "react-icons/md";

function CertificateScanner(){

    return(

        <>

            <Navbar/>

            <main className="certificate-page">

                <section className="certificate-header">

                    <h1>

                        Certificate Scanner

                    </h1>

                    <p>

                        Analyze SSL/TLS Certificates for Quantum Vulnerabilities

                    </p>

                </section>

                <section className="certificate-card">

                    <div className="certificate-top">

                        <div className="certificate-icon">

                            <MdVerifiedUser/>

                        </div>

                        <div>

                            <h2>

                                SSL Certificate Analysis

                            </h2>

                            <p>

                                QuantumShield-X examines certificate strength, signature algorithms and post-quantum readiness.

                            </p>

                        </div>

                    </div>

                    <div className="certificate-grid">

                        <div className="certificate-item">

                            <MdFingerprint className="cert-icon"/>

                            <div>

                                <h3>

                                    Signature Algorithm

                                </h3>

                                <p>

                                    RSA-2048

                                </p>

                            </div>

                        </div>

                        <div className="certificate-item">

                            <MdLock className="cert-icon"/>

                            <div>

                                <h3>

                                    Public Key

                                </h3>

                                <p>

                                    2048 Bits

                                </p>

                            </div>

                        </div>

                        <div className="certificate-item">

                            <MdWarning className="cert-icon warning"/>

                            <div>

                                <h3>

                                    Quantum Status

                                </h3>

                                <p>

                                    Vulnerable

                                </p>

                            </div>

                        </div>
                                                <div className="certificate-item">

                            <MdSecurity className="cert-icon success"/>

                            <div>

                                <h3>

                                    Recommended PQC

                                </h3>

                                <p>

                                    CRYSTALS-Kyber

                                </p>

                            </div>

                        </div>

                    </div>

                    <div className="recommendation-card">

                        <h2>

                            AI Recommendation

                        </h2>

                        <p>

                            Your certificate currently uses RSA-2048, which is vulnerable to future quantum attacks using Shor's Algorithm.

                        </p>

                        <div className="recommendation-box">

                            <strong>

                                Suggested Migration

                            </strong>

                            <span>

                                Replace RSA-2048 with ML-KEM (CRYSTALS-Kyber) for key exchange and ML-DSA (Dilithium) for digital signatures.

                            </span>

                        </div>

                    </div>

                    <div className="certificate-score">

                        <div className="score-card">

                            <h3>

                                Security Score

                            </h3>

                            <h1>

                                42%

                            </h1>

                        </div>

                        <div className="score-card">

                            <h3>

                                Quantum Readiness

                            </h3>

                            <h1>

                                Low

                            </h1>

                        </div>

                        <div className="score-card">

                            <h3>

                                Migration Priority

                            </h3>

                            <h1>

                                High

                            </h1>

                        </div>

                    </div>

                </section>

            </main>

        </>

    );

}

export default CertificateScanner;