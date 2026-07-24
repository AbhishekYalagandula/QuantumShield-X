import "./XAIInsights.css";
import { useEffect, useState } from "react";
import axios from "axios";

function XAIInsights() {

    const [insights, setInsights] = useState([]);

    useEffect(() => {

        loadInsights();

    }, []);

    const loadInsights = async () => {

        try {

            const response = await axios.get(
                "http://127.0.0.1:8000/xai/"
            );

            setInsights(response.data);

        }

        catch(err){

            console.log(err);

        }

    };

    return (

        <div className="xai-card">

            <h2>Explainable AI Insights</h2>

            <p>
                AI explains why every detected algorithm is risky.
            </p>

            <div className="xai-list">

                {

                    insights.map((item,index)=>(

                        <div
                            className="xai-item"
                            key={index}
                        >

                            <h3>{item.algorithm}</h3>

                            <p>

                                <strong>Risk:</strong> {item.risk}

                            </p>

                            <p>

                                <strong>Reason:</strong> {item.reason}

                            </p>

                            <p>

                                <strong>Quantum Attack:</strong> {item.quantum_attack}

                            </p>

                            <p>

                                <strong>Recommendation:</strong> {item.recommendation}

                            </p>

                            <p>

                                <strong>AI Confidence:</strong> {item.confidence}

                            </p>

                        </div>

                    ))

                }

            </div>

        </div>

    );

}

export default XAIInsights;