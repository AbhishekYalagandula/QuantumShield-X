import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Upload from "./pages/Upload";
import Scanner from "./pages/Scanner";

import CertificateScanner from "./pages/CertificateScanner";
import RiskAnalyzer from "./pages/RiskAnalyzer";
import AIRecommendation from "./pages/AIRecommendation";
import MigrationPlanner from "./pages/MigrationPlanner";
import Settings from "./pages/Settings";
import RiskReport from "./pages/RiskReport";
function App() {
  return (
    <Routes>

      <Route path="/" element={<Login />} />

      <Route path="/dashboard" element={<Dashboard />} />

      <Route path="/upload" element={<Upload />} />

      <Route path="/scanner" element={<Scanner />} />

      <Route path="/certificate" element={<CertificateScanner />} />

      <Route path="/risk" element={<RiskAnalyzer />} />

      <Route path="/recommendation" element={<AIRecommendation />} />

      <Route path="/migration" element={<MigrationPlanner />} />

      <Route path="/report" element={<RiskReport />} />

      <Route path="/settings" element={<Settings />} />

    </Routes>
  );
}

export default App;