import "./MigrationPlanner.css";

import Navbar from "../components/Navbar/Navbar";

import {

    MdSwapHoriz,

    MdSchedule,

    MdTrendingUp,

    MdConstruction

} from "react-icons/md";

import { useEffect, useState } from "react";

function MigrationPlanner(){

    const [migrationPlan, setMigrationPlan] = useState([]);

useEffect(() => {

    const downloadReport = () => {

    window.open(

        "http://127.0.0.1:8000/report/latest_report.txt",

        "_blank"

    );

};

    fetch("http://127.0.0.1:8000/migration/")

        .then(res => res.json())

        .then(data => {

            setMigrationPlan(data);

        })

        .catch(err => console.log(err));

}, []);

    return(

        <>

            <Navbar/>

            <main className="migration-page">

                <section className="migration-header">

                    <h1>

                        Migration Planner

                    </h1>

                    <p>

                        AI-generated roadmap for migrating vulnerable cryptographic algorithms to Post-Quantum Cryptography.

                    </p>

                </section>

                <section className="migration-card">

                    <div className="migration-top">

                        <div className="migration-icon">

                            <MdSwapHoriz/>

                        </div>

                        <div>

                            <h2>

                                Migration Roadmap

                            </h2>

                            <p>

                                QuantumShield-X automatically generates a prioritized migration plan based on your project's cryptographic risks.

                            </p>

                        </div>

                    </div>

                    <div className="migration-grid">

{

migrationPlan.map((item,index)=>(

<div
className="migration-item"
key={index}
>

<MdSwapHoriz className="migration-item-icon"/>

<div>

<h3>

{item.algorithm}

</h3>

<p>

→ {item.replace_with}

</p>

<small>

Priority : {item.priority}

</small>

<br/>

<small>

Difficulty : {item.difficulty}

</small>

<br/>

<small>

Time : {item.estimated_time}

</small>

</div>

</div>

))

}

</div>

                                                <div className="planner-section">

                            <h2>

                                Migration Plan

                            </h2>

                            <div className="planner-step">

                                <div className="step-icon">

                                    1

                                </div>

                                <div>

                                    <h3>

                                        Identify Vulnerable Algorithms

                                    </h3>

                                    <p>

                                        Detect RSA, ECC and other quantum vulnerable cryptographic algorithms.

                                    </p>

                                </div>

                            </div>

                            <div className="planner-step">

                                <div className="step-icon">

                                    2

                                </div>

                                <div>

                                    <h3>

                                        Replace with PQC Standards

                                    </h3>

                                    <p>

                                        Migrate to ML-KEM (CRYSTALS-Kyber) and ML-DSA (Dilithium).

                                    </p>

                                </div>

                            </div>

                            <div className="planner-step">

                                <div className="step-icon">

                                    3

                                </div>

                                <div>

                                    <h3>

                                        Validate Security

                                    </h3>

                                    <p>

                                        Perform automated verification and compatibility testing using QuantumShield-X.

                                    </p>

                                </div>

                            </div>

                        </div>

                        <div className="migration-progress">

                            <h2>

                                Migration Progress

                            </h2>

                            <div className="progress-bar">

                                <div

                                    className="progress-fill"

                                    style={{

                                        width:`${Math.min(migrationPlan.length*20,100)}%`

                                    }}

                                >

                                </div>

                            </div>

                            <span>

                                41% Migration Completed

                            </span>

                        </div>
                                            <div className="planner-summary">

                        <div className="planner-card">

                            <h3>

                                Algorithms to Migrate

                            </h3>

                           <h1>
    {migrationPlan.length}
</h1>

                        </div>

                        <div className="planner-card">

                            <h3>

                                Estimated Duration

                            </h3>
<h1>
    {
        migrationPlan.length > 0
        ? migrationPlan[0].estimated_time
        : "-"
    }
</h1>

                        </div>

                        <div className="planner-card">

                            <h3>

                                Current Status

                            </h3>

                            <h1>
    {
        migrationPlan.length > 0
        ? migrationPlan[0].status
        : "-"
    }
</h1>

                        </div>

                    </div>

                    <div className="planner-footer">

                        <button

    className="planner-btn"

    onClick={downloadReport}

>

    Generate Migration Report

</button>

                    </div>

                </section>

            </main>

        </>

    );

}

export default MigrationPlanner;