from qiskit.circuit.library import ZZFeatureMap


def get_feature_map():

    """
    Creates the Quantum Feature Map used by the
    Variational Quantum Classifier.
    """

    feature_map = ZZFeatureMap(

        feature_dimension=4,
        reps=2

    )

    return feature_map