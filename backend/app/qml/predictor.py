from qiskit_algorithms.optimizers import COBYLA
from qiskit.primitives import StatevectorSampler
from qiskit_machine_learning.algorithms.classifiers import VQC

from app.qml.dataset import get_training_data
from app.qml.feature_map import get_feature_map
from app.qml.ansatz import get_ansatz
from app.quantum.feature_encoder import encode_features


_classifier = None


def load_classifier():
    """
    Train the VQC once and reuse it.
    """

    global _classifier

    if _classifier is None:

        X, y = get_training_data()

        feature_map = get_feature_map()

        ansatz = get_ansatz()

        optimizer = COBYLA(maxiter=100)

        sampler = StatevectorSampler()

        _classifier = VQC(
            sampler=sampler,
            feature_map=feature_map,
            ansatz=ansatz,
            optimizer=optimizer
        )

        _classifier.fit(X, y)

        print("✅ Quantum VQC Loaded")

    return _classifier


def predict_project(analysis):
    """
    Predict project risk using Quantum ML.
    """

    classifier = load_classifier()

    features = encode_features(analysis)

    X = []

    for item in features:

        X.append([
            1 if item["algorithm"] == "RSA" else 0,
            1 if item["algorithm"] == "ECC" else 0,
            1 if item["algorithm"] == "SHA-1" else 0,
            1 if item["algorithm"] == "TLS" else 0
        ])

    predictions = classifier.predict(X)

    return predictions.tolist()