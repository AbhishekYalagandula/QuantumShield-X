import Navbar from "./Navbar";
import "./Dashboard.css";
import StatsCard from "./StatsCard";
import RiskGauge from "./RiskGauge";
import RecentScans from "./RecentScans";
import QuickActions from "./QuickActions";
import RiskTrend from "./RiskTrend";


function Dashboard() {
  return (
    <div className="dashboard">

      <Navbar />
      <div className="stats-container">

<StatsCard
title="Projects"
value="15"
icon="📁"
/>

<StatsCard
title="High Risk"
value="4"
icon="⚠"
/>

<StatsCard
title="Secure Files"
value="11"
icon="🛡"
/>

<StatsCard
title="Reports"
value="8"
icon="📄"
/>
<div className="dashboard-row">

    <RiskGauge/>

    <RecentScans/>

    <QuickActions />

    <RiskTrend />

</div>

</div>

      <div className="dashboard-content">

        <h1>Dashboard</h1>

        <p>
          Welcome to QuantumShield-X
        </p>

      </div>

    </div>
  );
}

export default Dashboard;