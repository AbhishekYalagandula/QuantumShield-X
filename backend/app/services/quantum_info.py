from qiskit import transpile


def get_quantum_metadata(qc, backend, shots=1024):
    """
    Returns metadata about the executed quantum circuit.
    """

    compiled = transpile(qc, backend)

    return {
        "backend": backend.name,
        "qubits": qc.num_qubits,
        "depth": compiled.depth(),
        "width": compiled.width(),
        "size": compiled.size(),
        "shots": shots,
        "status": "Executed Successfully"
    }