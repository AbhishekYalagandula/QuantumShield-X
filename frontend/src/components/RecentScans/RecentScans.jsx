import "./RecentScans.css";

import { useEffect, useState } from "react";
import axios from "axios";

import {
    MdFolder,
    MdVisibility,
    MdWarning,
    MdCheckCircle
} from "react-icons/md";

function RecentScans() {

    const [scans, setScans] = useState([]);

    useEffect(() => {

        loadRecentScans();

    }, []);

    const loadRecentScans = async () => {

        try {

            const response = await axios.get(
                "http://127.0.0.1:8000/dashboard/recent-scans"
            );

            setScans(response.data);

        } catch (error) {

            console.error(error);

        }

    };

    return (

        <div className="recent-card">

            <div className="recent-header">

                <div>

                    <h2>
                        Recent Security Scans
                    </h2>

                    <p>
                        Latest analyzed software projects
                    </p>

                </div>

                <button className="recent-btn">

                    View All

                </button>

            </div>

           <div className="recent-list">

    {

        scans.length === 0 ?

        (

            <div className="no-scans">

                No Projects Scanned Yet

            </div>

        )

        :

        scans.map((scan) => (
            

                        <div
                            className="scan-item"
                            key={scan.id}
                        >

                            <div className="scan-left">

                                <div className="scan-icon">

                                    <MdFolder />

                                </div>

                                <div className="scan-info">

                                    <h3>

                                        {scan.project_name}

                                    </h3>

                                    <span>

                                        {new Date(scan.upload_time).toLocaleString()}

                                    </span>

                                </div>

                            </div>

                            <div className="scan-center">

                                <span className="algo-count">

                                    Risk Score : {scan.risk_score}

                                </span>

                            </div>

                            <div className="scan-right">

                                <span
                                    className={`risk-badge ${scan.risk_level.toLowerCase()}`}
                                >

                                    {

                                        scan.risk_level === "Critical" ||

                                        scan.risk_level === "High"

                                            ?

                                            <MdWarning />

                                            :

                                            <MdCheckCircle />

                                    }

                                    {scan.risk_level}

                                </span>

                                <button
                                    className="view-btn"
                                >

                                    <MdVisibility />

                                </button>

                            </div>

                        </div>

                    ))

                }

            </div>

            <div className="recent-footer">

                <span>

                    Showing latest security assessments

                </span>

                <button className="footer-btn">

                    Open Dashboard Logs

                </button>

            </div>

        </div>

    );

}

export default RecentScans;