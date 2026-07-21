import "./RiskGauge.css";

function RiskGauge({

    score = 74,
    risk = "Medium"

}) {

    const radius = 90;

    const stroke = 14;

    const normalizedRadius = radius - stroke;

    const circumference = normalizedRadius * 2 * Math.PI;

    const offset =
        circumference -
        (score / 100) * circumference;

    return (

        <div className="risk-gauge-card">

            <div className="risk-header">

                <div>

                    <h2>

                        Quantum Risk

                    </h2>

                    <p>

                        Overall organization security posture

                    </p>

                </div>

            </div>

            <div className="gauge-wrapper">

    <svg
        height={radius * 2}
        width={radius * 2}
        className="risk-svg"
    >

        <circle
            stroke="#1b2b4d"
            fill="transparent"
            strokeWidth={stroke}
            r={normalizedRadius}
            cx={radius}
            cy={radius}
        />

        <circle
            className="progress-circle"
            stroke="url(#gradient)"
            fill="transparent"
            strokeWidth={stroke}
            strokeDasharray={`${circumference} ${circumference}`}
            strokeDashoffset={offset}
            strokeLinecap="round"
            r={normalizedRadius}
            cx={radius}
            cy={radius}
        />

        <defs>

            <linearGradient
                id="gradient"
                x1="0%"
                y1="0%"
                x2="100%"
                y2="100%"
            >

                <stop offset="0%" stopColor="#6C63FF" />

                <stop offset="100%" stopColor="#3B82F6" />

            </linearGradient>

        </defs>

    </svg>

    <div className="gauge-content">

        <h1>{score}%</h1>

        <span>{risk} Risk</span>

    </div>

</div>

<div className="risk-status">

    <div className="status-item">

        <span className="status-label">

            Quantum Readiness

        </span>

        <strong>68%</strong>

    </div>

    <div className="status-item">

        <span className="status-label">

            Vulnerable Algorithms

        </span>

        <strong>12</strong>

    </div>

    <div className="status-item">

        <span className="status-label">

            Migration Progress

        </span>

        <strong>41%</strong>

    </div>

</div>

<div className="risk-footer">

                <div className="risk-indicator">

                    <span className="indicator-dot"></span>

                    <span>

                        Live Security Assessment

                    </span>

                </div>

                <button className="risk-btn">

                    View Details

                </button>

            </div>

        </div>

    );

}

export default RiskGauge;