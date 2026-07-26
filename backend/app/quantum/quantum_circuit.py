from qiskit import QuantumCircuit

import os
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use("Agg")

def build_quantum_circuit(features, filename="latest"):
    """
    Build a quantum circuit and save its image.
    """

    num_qubits = len(features)

    if num_qubits == 0:
        num_qubits = 1

        features = [
            {
                "algorithm": "None",
                "risk": "Safe",
                "theta": 0
            }
        ]

    qc = QuantumCircuit(num_qubits, num_qubits)

    # -------------------------
    # Encode Features
    # -------------------------

    for index, feature in enumerate(features):

        qc.ry(feature["theta"], index)

    # -------------------------
    # Entangle
    # -------------------------

    for i in range(num_qubits - 1):

        qc.cx(i, i + 1)

    # -------------------------
    # Measurement
    # -------------------------

    qc.measure(range(num_qubits), range(num_qubits))

    # -------------------------
    # Save Circuit Image
    # -------------------------

    output_folder = "app/static/circuits"

    os.makedirs(output_folder, exist_ok=True)

    image_path = os.path.join(
        output_folder,
        f"{filename}.png"
    )

    figure = qc.draw(output="mpl")

    figure.savefig(image_path)

    plt.close(figure)

    return qc, image_path