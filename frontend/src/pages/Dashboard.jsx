import "./Dashboard.css";

import Navbar from "../components/Navbar/Navbar";
import StatsCard from "../components/StatsCard/StatsCard";
import RiskGauge from "../components/RiskGauge/RiskGauge";
import RiskTrend from "../components/RiskTrend/RiskTrend";
import RecentScans from "../components/RecentScans/RecentScans";
import QuickActions from "../components/QuickActions/QuickActions";

import {
    MdFolder,
    MdWarning,
    MdSecurity,
    MdAnalytics
} from "react-icons/md";

function Dashboard(){

    return(

        <>

            <Navbar/>

            <main className="dashboard">

                {/* ==========================
                        PAGE HEADER
                ========================== */}

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

                {/* ==========================
                        STATS
                ========================== */}

                <section className="stats-grid">

                    <StatsCard

                        icon={<MdFolder/>}

                        title="Projects"

                        value="26"

                        change="+5"

                        positive={true}

                    />

                    <StatsCard

                        icon={<MdWarning/>}

                        title="Critical Risks"

                        value="8"

                        change="-2"

                        positive={false}

                    />

                    <StatsCard

                        icon={<MdSecurity/>}

                        title="PQC Ready"

                        value="74%"

                        change="+12%"

                        positive={true}

                    />

                    <StatsCard

                        icon={<MdAnalytics/>}

                        title="Today's Scans"

                        value="41"

                        change="+9"

                        positive={true}

                    />

                </section>
                                {/* ==========================
                        ANALYTICS
                ========================== */}

                <section className="analytics-grid">

                    <div className="analytics-left">

                        <RiskGauge

                            score={74}

                            risk="Medium"

                        />

                    </div>

                    <div className="analytics-right">

                        <RiskTrend/>

                    </div>

                </section>

                {/* ==========================
                        BOTTOM GRID
                ========================== */}

                <section className="bottom-grid">

                    <div className="bottom-left">

                        <RecentScans/>

                    </div>

                    <div className="bottom-right">

                        <QuickActions/>

                    </div>

                </section>

            </main>

        </>

    );

}

export default Dashboard;