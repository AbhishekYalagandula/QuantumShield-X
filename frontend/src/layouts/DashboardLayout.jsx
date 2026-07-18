import "./DashboardLayout.css";

import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";

function DashboardLayout({ children }) {

    return (

        <div className="layout">

            <Sidebar />

            <div className="layout-main">

                <Navbar />

                <main className="layout-content">

                    {children}

                </main>

            </div>

        </div>

    );

}

export default DashboardLayout;