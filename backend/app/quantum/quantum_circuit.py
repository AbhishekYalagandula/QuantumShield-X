from qiskit import QuantumCircuit
import os
import matplotlib.pyplot as plt


def build_quantum_circuit(features):
    """
    Build a quantum circuit from encoded features.
    """

    # ------------------------------------
    # Number of qubits
    # ------------------------------------

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

    # ------------------------------------
    # Create Quantum Circuit
    # ------------------------------------

    qc = QuantumCircuit(num_qubits, num_qubits)

    # ------------------------------------
    # Encode Features
    # ------------------------------------

    for index, feature in enumerate(features):

        theta = feature["theta"]

        qc.ry(theta, index)

    # ------------------------------------
    # Entangle Qubits
    # ------------------------------------

    for i in range(num_qubits - 1):

        qc.cx(i, i + 1)

    # ------------------------------------
    # Measurement
    # ------------------------------------

    qc.measure(range(num_qubits), range(num_qubits))

    # ------------------------------------
    # Save Quantum Circuit Image
    # ------------------------------------

    output_folder = "app/static/circuits"

    os.makedirs(output_folder, exist_ok=True)

    image_path = os.path.join(
        output_folder,
        "latest_circuit.png"
    )

    figure = qc.draw(output="mpl")

    figure.savefig(image_path)

    plt.close(figure)

    # ------------------------------------
    # Return Circuit
    # ------------------------------------

    return qc