import "./QuickActions.css";

import {

    MdUpload,

    MdSearch,

    MdSecurity,

    MdPsychology,

    MdTimeline,

    MdDescription

} from "react-icons/md";

const actions = [

    {

        id:1,

        title:"Upload Project",

        icon:<MdUpload/>,

        color:"blue"

    },

    {

        id:2,

        title:"Start Scan",

        icon:<MdSearch/>,

        color:"purple"

    },

    {

        id:3,

        title:"Risk Analyzer",

        icon:<MdSecurity/>,

        color:"red"

    },

    {

        id:4,

        title:"AI Recommendation",

        icon:<MdPsychology/>,

        color:"green"

    },

    {

        id:5,

        title:"Migration Planner",

        icon:<MdTimeline/>,

        color:"orange"

    },

    {

        id:6,

        title:"Generate Report",

        icon:<MdDescription/>,

        color:"cyan"

    }

];

function QuickActions(){

    return(

        <div className="quick-card">

            <div className="quick-header">

                <div>

                    <h2>

                        Quick Actions

                    </h2>

                    <p>

                        Launch QuantumShield-X modules instantly

                    </p>

                </div>

            </div>

            <div className="quick-grid">
                              {

                    actions.map((action)=>(

                        <button

                            key={action.id}

                            className={`action-card ${action.color}`}

                        >

                            <div className="action-icon">

                                {action.icon}

                            </div>

                            <div className="action-content">

                                <h3>

                                    {action.title}

                                </h3>

                                <span>

                                    Click to Launch

                                </span>

                            </div>

                        </button>

                    ))

                }

            </div>
                        <div className="quick-footer">

                <span>

                    Choose any module to start your security workflow

                </span>

                <button className="workflow-btn">

                    Start Complete Security Workflow

                </button>

            </div>

        </div>

    );

}

export default QuickActions;