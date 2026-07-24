import "./QuantumCircuitViewer.css";

function QuantumCircuitViewer() {

    return (

        <div className="quantum-card">

            <h2>Quantum Circuit</h2>

            <p>
                Live Qiskit Circuit Visualization
            </p>

            <div className="circuit-box">

                <pre>

{`q0 ──RY──■────────M
          │
q1 ──RY───X──■─────M
             │
q2 ──RY──────X──■──M
                │
q3 ──RY─────────X──M`}

                </pre>

            </div>

        </div>

    );

}

export default QuantumCircuitViewer;