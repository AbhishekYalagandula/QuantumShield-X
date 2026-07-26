from qiskit_algorithms.optimizers import COBYLA

from qiskit.primitives import StatevectorSampler

from qiskit_machine_learning.algorithms.classifiers import VQC

from app.qml.dataset import get_training_data
from app.qml.feature_map import get_feature_map
from app.qml.ansatz import get_ansatz


MODEL_PATH = "app/qml/vqc_model.pkl"


def train_vqc():

    """
    Train the Variational Quantum Classifier.
    """

    # -----------------------------
    # Load Dataset
    # -----------------------------

    X, y = get_training_data()

    # -----------------------------
    # Feature Map
    # -----------------------------

    feature_map = get_feature_map()

    # -----------------------------
    # Ansatz
    # -----------------------------

    ansatz = get_ansatz()

    # -----------------------------
    # Optimizer
    # -----------------------------

    optimizer = COBYLA(maxiter=100)

    # -----------------------------
    # Sampler
    # -----------------------------

    sampler = StatevectorSampler()

    # -----------------------------
    # Create VQC
    # -----------------------------

    classifier = VQC(
        sampler=sampler,
        feature_map=feature_map,
        ansatz=ansatz,
        optimizer=optimizer
    )

    # -----------------------------
    # Train
    # -----------------------------

    classifier.fit(X, y)

    # -----------------------------
    # Save Model
    # -----------------------------

    print("\n===================================")
    print("✅ Quantum VQC Model Trained Successfully")
    print("===================================")

    return classifier


if __name__ == "__main__":

    train_vqc()