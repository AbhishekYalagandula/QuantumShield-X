import "./Sidebar.css";

import {
    MdDashboard,
    MdCloudUpload,
    MdSecurity,
    MdOutlineAssessment,
    MdSettings,
    MdLogout,
    MdVerifiedUser,
    MdDescription
} from "react-icons/md";

import {
    FaRobot,
    FaProjectDiagram
} from "react-icons/fa";

import {
    HiMenuAlt2
} from "react-icons/hi";

import {
    useNavigate,
    useLocation
} from "react-router-dom";

function Sidebar() {

    const navigate = useNavigate();
    const location = useLocation();

    const menuItems = [

        {
            title: "Dashboard",
            icon: <MdDashboard />,
            path: "/dashboard"
        },

        {
            title: "Upload Project",
            icon: <MdCloudUpload />,
            path: "/upload"
        },

        {
            title: "Code Scanner",
            icon: <MdSecurity />,
            path: "/scanner"
        },

        {
            title: "Certificate Scanner",
            icon: <MdVerifiedUser />,
            path: "/certificate"
        },

        {
            title: "Risk Analyzer",
            icon: <MdOutlineAssessment />,
            path: "/risk"
        },

        {
            title: "AI Recommendation",
            icon: <FaRobot />,
            path: "/recommendation"
        },

        {
            title: "Migration Planner",
            icon: <FaProjectDiagram />,
            path: "/migration"
        },

        {
            title: "Reports",
            icon: <MdDescription />,
            path: "/report"
        },

        {
            title: "Settings",
            icon: <MdSettings />,
            path: "/settings"
        }

    ];

    function logout(){

        localStorage.removeItem("access_token");

        navigate("/");

    }

    return(

        <aside className="sidebar">

            {/* ===========================
                    Logo
            ============================ */}

            <div className="sidebar-header">

                <div className="logo">

                    <div className="logo-icon">

                        🛡

                    </div>

                    <div className="logo-text">

                        <h2>QuantumShield-X</h2>

                        <span>Enterprise Security</span>

                    </div>

                </div>

                <button className="menu-button">

                    <HiMenuAlt2 />

                </button>

            </div>

            {/* ===========================
                    Navigation
            ============================ */}

            <nav className="sidebar-menu">

                {

                    menuItems.map((item,index)=>(

                        <button

                            key={index}

                            className={`menu-item ${
                                location.pathname===item.path
                                ? "active"
                                : ""
                            }`}

                            onClick={()=>navigate(item.path)}

                        >

                            <div className="menu-icon">

                                {item.icon}

                            </div>

                            <span>

                                {item.title}

                            </span>

                        </button>

                    ))

                }

            </nav>
                        {/* ===========================
                    User Profile
            ============================ */}

            <div className="sidebar-user">

                <div className="user-avatar">

                    A

                </div>

                <div className="user-info">

                    <h4>Abhishek</h4>

                    <span>Administrator</span>

                </div>

                <div className="online-dot"></div>

            </div>

            {/* ===========================
                    Logout
            ============================ */}

            <div className="sidebar-footer">

                <button
                    className="logout-button"
                    onClick={logout}
                >

                    <MdLogout />

                    <span>

                        Logout

                    </span>

                </button>

            </div>

        </aside>

    );

}

export default Sidebar;