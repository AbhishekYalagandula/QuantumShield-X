import "./RecentScans.css";

function RecentScans() {

    const scans = [

        {
            project: "BankingApp.zip",
            risk: "High"
        },

        {
            project: "Ecommerce.zip",
            risk: "Medium"
        },

        {
            project: "InternalTools.zip",
            risk: "Low"
        }

    ];

    return (

        <div className="recent-box">

            <h2>Recent Scans</h2>

            {

                scans.map((scan,index)=>(

                    <div className="scan-item" key={index}>

                        <div>

                            📄 {scan.project}

                        </div>

                        <span className={scan.risk.toLowerCase()}>

                            {scan.risk}

                        </span>

                    </div>

                ))

            }

        </div>

    );

}

export default RecentScans;