from qiskit.circuit.library import RealAmplitudes


def get_ansatz():

    """
    Trainable Quantum Circuit (Ansatz)
    used by the Variational Quantum Classifier.
    """

    ansatz = RealAmplitudes(

        num_qubits=4,
        reps=2,
        entanglement="full"

    )

    return ansatz