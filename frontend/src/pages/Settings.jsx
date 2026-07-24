import "./Settings.css";

import Navbar from "../components/Navbar/Navbar";

import {

    MdSettings,

    MdPerson,

    MdNotifications,

    MdSecurity,

    MdStorage

} from "react-icons/md";

function Settings(){

    return(

        <>

            <Navbar/>

            <main className="settings-page">

                <section className="settings-header">

                    <h1>

                        Settings

                    </h1>

                    <p>

                        Manage QuantumShield-X preferences, security and system configuration.

                    </p>

                </section>

                <section className="settings-card">

                    <div className="settings-top">

                        <div className="settings-icon">

                            <MdSettings/>

                        </div>

                        <div>

                            <h2>

                                Application Settings

                            </h2>

                            <p>

                                Configure user preferences and system behaviour for QuantumShield-X.

                            </p>

                        </div>

                    </div>

                    <div className="settings-grid">

                        <div className="setting-item">

                            <MdPerson className="setting-item-icon"/>

                            <div>

                                <h3>

                                    User Profile

                                </h3>

                                <p>

                                    Admin User

                                </p>

                            </div>

                        </div>

                        <div className="setting-item">

                            <MdNotifications className="setting-item-icon"/>

                            <div>

                                <h3>

                                    Notifications

                                </h3>

                                <p>

                                    Enabled

                                </p>

                            </div>

                        </div>

                        <div className="setting-item">

                            <MdSecurity className="setting-item-icon"/>

                            <div>

                                <h3>

                                    Security Mode

                                </h3>

                                <p>

                                    High Protection

                                </p>

                            </div>

                        </div>

                        <div className="setting-item">

                            <MdStorage className="setting-item-icon"/>

                            <div>

                                <h3>

                                    Database

                                </h3>

                                <p>

                                    SQLite Connected

                                </p>

                            </div>

                        </div>

                    </div>
                                        <div className="settings-section">

                        <h2>

                            System Configuration

                        </h2>

                        <div className="config-item">

                            <div>

                                <h3>

                                    Automatic Security Scan

                                </h3>

                                <p>

                                    Scan uploaded projects immediately after upload.

                                </p>

                            </div>

                            <label className="switch">

                                <input
                                    type="checkbox"
                                    defaultChecked
                                />

                                <span className="slider"></span>

                            </label>

                        </div>

                        <div className="config-item">

                            <div>

                                <h3>

                                    AI Recommendation Engine

                                </h3>

                                <p>

                                    Enable intelligent post-quantum migration recommendations.

                                </p>

                            </div>

                            <label className="switch">

                                <input
                                    type="checkbox"
                                    defaultChecked
                                />

                                <span className="slider"></span>

                            </label>

                        </div>

                        <div className="config-item">

                            <div>

                                <h3>

                                    Email Notifications

                                </h3>

                                <p>

                                    Receive alerts when critical vulnerabilities are detected.

                                </p>

                            </div>

                            <label className="switch">

                                <input
                                    type="checkbox"
                                />

                                <span className="slider"></span>

                            </label>

                        </div>

                    </div>

                    <div className="system-status">

                        <h2>

                            System Status

                        </h2>

                        <div className="status-grid">

                            <div className="status-card">

                                <h3>

                                    Backend API

                                </h3>

                                <span className="online">

                                    ● Online

                                </span>

                            </div>

                            <div className="status-card">

                                <h3>

                                    Database

                                </h3>

                                <span className="online">

                                    ● Connected

                                </span>

                            </div>

                            <div className="status-card">

                                <h3>

                                    AI Engine

                                </h3>

                                <span className="online">

                                    ● Ready

                                </span>

                            </div>

                        </div>

                    </div>
                                        <div className="settings-footer">

                        <button className="save-btn">

                            Save Settings

                        </button>

                    </div>

                </section>

            </main>

        </>

    );

}

export default Settings;