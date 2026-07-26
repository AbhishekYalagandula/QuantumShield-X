import time


def generate_quantum_metadata(
    circuit,
    execution_time,
    shots=1024,
    backend="IBM Aer Simulator"
):

    metadata = {}

    metadata["qubits"] = circuit.num_qubits

    metadata["depth"] = circuit.depth()

    metadata["gates"] = sum(circuit.count_ops().values())

    operations = circuit.count_ops()

    metadata["cx_gates"] = operations.get("cx", 0)

    metadata["ry_gates"] = operations.get("ry", 0)

    metadata["measurements"] = operations.get("measure", 0)

    metadata["backend"] = backend

    metadata["shots"] = shots

    metadata["execution_time"] = f"{execution_time:.2f} ms"

    return metadata