import numpy as np


def get_training_data():
    """
    Training dataset for Quantum Machine Learning.
    Features:
    [RSA, ECC, SHA1, TLS]

    Labels:
    1 = High Quantum Risk
    0 = Low Quantum Risk
    """

    X = np.array([

        [1, 0, 1, 0],   # RSA + SHA1
        [1, 1, 1, 1],   # RSA + ECC + SHA1 + TLS
        [1, 0, 0, 1],   # RSA + TLS
        [0, 1, 1, 0],   # ECC + SHA1
        [0, 0, 0, 0],   # Safe
        [0, 0, 0, 1],   # TLS only
        [0, 0, 1, 0],   # SHA1 only
        [0, 1, 0, 0],   # ECC only

    ])

    y = np.array([

        1,
        1,
        1,
        1,
        0,
        0,
        0,
        0

    ])

    return X, y