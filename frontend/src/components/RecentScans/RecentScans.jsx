import "./RecentScans.css";

import {

    MdFolder,

    MdVisibility,

    MdWarning,

    MdCheckCircle

} from "react-icons/md";

const scans = [

    {

        id:1,

        project:"E-Commerce Backend",

        time:"2 mins ago",

        risk:"High",

        algorithms:12

    },

    {

        id:2,

        project:"Hospital Management",

        time:"15 mins ago",

        risk:"Medium",

        algorithms:7

    },

    {

        id:3,

        project:"Banking API",

        time:"42 mins ago",

        risk:"Low",

        algorithms:3

    }

];

function RecentScans(){

    return(

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

                    scans.map((scan)=>(

                        <div

                            className="scan-item"

                            key={scan.id}

                        >

                            <div className="scan-left">

                                <div className="scan-icon">

                                    <MdFolder/>

                                </div>

                                <div className="scan-info">

                                    <h3>

                                        {scan.project}

                                    </h3>

                                    <span>

                                        {scan.time}

                                    </span>

                                </div>

                            </div>

                            <div className="scan-center">

                                <span className="algo-count">

                                    {scan.algorithms}

                                    {" "}Algorithms

                                </span>

                            </div>

                            <div className="scan-right">

                                <span

                                    className={`risk-badge ${scan.risk.toLowerCase()}`}

                                >

                                    {

                                        scan.risk==="High"

                                        ?

                                        <MdWarning/>

                                        :

                                        <MdCheckCircle/>

                                    }

                                    {scan.risk}

                                </span>

                                <button

                                    className="view-btn"

                                >

                                    <MdVisibility/>

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
