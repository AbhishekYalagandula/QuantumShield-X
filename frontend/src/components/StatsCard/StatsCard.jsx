import "./StatsCard.css";

import {
    MdTrendingUp,
    MdTrendingDown
} from "react-icons/md";

function StatsCard({

    icon,
    title,
    value,
    change,
    positive

}){

    return(

        <div className="stats-card">

            <div className="stats-top">

                <div className="stats-icon">

                    {icon}

                </div>

                <div
                    className={`stats-change ${
                        positive
                        ? "positive"
                        : "negative"
                    }`}
                >

                    {

                        positive
                        ?

                        <MdTrendingUp/>

                        :

                        <MdTrendingDown/>

                    }

                    <span>

                        {change}

                    </span>

                </div>

            </div>

            <div className="stats-content">

                <h3>

                    {value}

                </h3>

                <p>

                    {title}

                </p>

            </div>

        </div>

    );

}

export default StatsCard;