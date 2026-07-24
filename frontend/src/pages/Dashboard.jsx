import "./Dashboard.css";

import { useEffect, useState } from "react";

import axios from "axios";
import DashboardLayout from "../layouts/DashboardLayout";

import QuantumCircuitViewer
from "../components/QuantumCircuitViewer/QuantumCircuitViewer";

import StatsCard from "../components/StatsCard/StatsCard";
import RiskGauge from "../components/RiskGauge/RiskGauge";
import RiskTrend from "../components/RiskTrend/RiskTrend";
import RecentScans from "../components/RecentScans/RecentScans";
import QuickActions from "../components/QuickActions/QuickActions";
import XAIInsights from "../components/XAIInsights/XAIInsights";

import {

    MdFolder,

    MdWarning,

    MdSecurity,

    MdAnalytics

} from "react-icons/md";

function Dashboard(){

    const [dashboardData,setDashboardData] = useState({

        projects:0,

        critical:0,

        pqc:0,

        today:0,

        risk_score:0,

        risk_level:"Loading..."

    });

    const [loading,setLoading] = useState(true);

    const [error,setError] = useState("");

    useEffect(()=>{

        fetchDashboard();

    },[]);

    const fetchDashboard = async()=>{

        try{

            const token = localStorage.getItem("access_token");

            const response = await axios.get(

                "http://127.0.0.1:8000/dashboard/summary",

                {

                    headers:{

                        Authorization:`Bearer ${token}`

                    }

                }

            );

            setDashboardData(response.data);

        }

        catch(err){

            console.error(err);

            setError("Unable to load dashboard.");

        }

        finally{

            setLoading(false);

        }

    };

    return(

        <DashboardLayout>

            <main className="dashboard">

                <section className="dashboard-header">

                    <div>

                        <h1>

                            QuantumShield-X Dashboard

                        </h1>

                        <p>

                            Monitor Quantum Risks, AI Recommendations and Security Status

                        </p>

                    </div>

                </section>
                                {

                    loading ?

                    (

                        <div className="dashboard-loading">

                            <h2>

                                Loading Dashboard...

                            </h2>

                        </div>

                    )

                    :

                    error ?

                    (

                        <div className="dashboard-error">

                            <h2>

                                {error}

                            </h2>

                        </div>

                    )

                    :

                    (

                        <>

                            {/* ==========================
                                    STATS
                            ========================== */}

                            <section className="stats-grid">

                                <StatsCard

                                    icon={<MdFolder/>}

                                    title="Projects"

                                    value={dashboardData.projects}

                                    change="+0"

                                    positive={true}

                                />

                                <StatsCard

                                    icon={<MdWarning/>}

                                    title="Critical Risks"

                                    value={dashboardData.critical}

                                    change="-0"

                                    positive={false}

                                />

                                <StatsCard

                                    icon={<MdSecurity/>}

                                    title="PQC Ready"

                                    value={`${dashboardData.pqc}%`}

                                    change="+0%"

                                    positive={true}

                                />

                                <StatsCard

                                    icon={<MdAnalytics/>}

                                    title="Today's Scans"

                                    value={dashboardData.today}

                                    change="+0"

                                    positive={true}

                                />

                            </section>

                            {/* ==========================
                                    ANALYTICS
                            ========================== */}

                            <XAIInsights />

                            <section className="analytics-grid">

                                <div className="analytics-left">

                                    <RiskGauge
    score={dashboardData.risk_score}
    risk={dashboardData.risk_level}
    pqc={dashboardData.pqc}
    vulnerable={dashboardData.vulnerable_algorithms}
    migration={dashboardData.migration_progress}
/>

                                </div>

                                <div className="analytics-right">

                                    <RiskTrend/>

                                </div>

                            </section>

                            <section className="quantum-section">

    <QuantumCircuitViewer/>

</section>

                                                        {/* ==========================
                                    BOTTOM GRID
                            ========================== */}

                            <section className="bottom-grid">

                                <div className="bottom-left">

                                    <RecentScans />

                                </div>

                                <div className="bottom-right">

                                    <QuickActions />

                                </div>

                            </section>

                        </>

                    )

                }

            </main>

        </DashboardLayout>

    );

}

export default Dashboard;