import "./Navbar.css";

import {
    MdNotificationsNone,
    MdSearch,
    MdCalendarToday
} from "react-icons/md";

function Navbar() {

    const today = new Date();

    const date = today.toLocaleDateString("en-IN",{
        weekday:"long",
        day:"numeric",
        month:"long",
        year:"numeric"
    });

    return(

        <header className="navbar">

            {/* Left */}

            <div className="navbar-left">

                <div>

                    <h1>

                        Dashboard

                    </h1>

                    <p>

                        Welcome back to QuantumShield-X

                    </p>

                </div>

            </div>

            {/* Center */}

            <div className="navbar-search">

                <MdSearch className="search-icon"/>

                <input

                    type="text"

                    placeholder="Search Projects, Reports..."

                />

            </div>

            {/* Right */}

            <div className="navbar-right">

                <div className="navbar-date">

                    <MdCalendarToday/>

                    <span>

                        {date}

                    </span>

                </div>

                <button className="notification-btn">

                    <MdNotificationsNone/>

                    <span className="notification-count">

                        3

                    </span>

                </button>
                                <div className="navbar-profile">

                    <div className="profile-info">

                        <h4>

                            Abhishek

                        </h4>

                        <span>

                            Security Administrator

                        </span>

                    </div>

                    <div className="profile-avatar">

                        A

                    </div>

                </div>

            </div>

        </header>

    );

}

export default Navbar;