import "./DashboardLayout.css";

import Sidebar from "../../components/Sidebar/Sidebar";
import Navbar from "../../components/Navbar/Navbar";

function DashboardLayout({ children }) {

    return (

        <div className="dashboard-layout">

            {/* Sidebar */}

            <aside className="dashboard-sidebar">

                <Sidebar />

            </aside>

            {/* Main Content */}

            <div className="dashboard-main">

                {/* Navbar */}

                <header className="dashboard-navbar">

                    <Navbar />

                </header>

                {/* Page */}

                <main className="dashboard-content">

                    {children}

                </main>

            </div>

        </div>

    );

}

export default DashboardLayout;