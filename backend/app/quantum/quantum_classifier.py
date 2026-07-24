from qiskit import transpile
from qiskit_aer import AerSimulator


def execute_quantum_circuit(qc):
    """
    Execute quantum circuit using Aer Simulator.
    """

    simulator = AerSimulator()

    compiled_circuit = transpile(qc, simulator)

    job = simulator.run(compiled_circuit, shots=1024)

    result = job.result()

    counts = result.get_counts(compiled_circuit)

    return counts