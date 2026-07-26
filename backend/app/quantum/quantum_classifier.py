from qiskit import transpile
from qiskit_aer import AerSimulator
import time


def execute_quantum_circuit(qc):
    """
    Execute quantum circuit using Aer Simulator.
    """

    simulator = AerSimulator()

    start = time.perf_counter()

    compiled_circuit = transpile(qc, simulator)

    job = simulator.run(compiled_circuit, shots=1024)

    result = job.result()

    counts = result.get_counts(compiled_circuit)

    end = time.perf_counter()

    execution_time = (end - start) * 1000

    return counts, execution_time