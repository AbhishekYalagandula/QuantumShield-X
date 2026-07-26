ALGORITHM_READINESS = {

    "RSA": 0,

    "ECC": 10,

    "ECDSA": 10,

    "SHA-1": 20,

    "SHA-256": 70,

    "SHA-3": 100,

    "TLS": 50,

    "TLS 1.3": 90,

    "AES": 100,

    "AES-256": 100,

    "ML-KEM": 100,

    "ML-DSA": 100
}


def calculate_quantum_readiness(analysis):

    scores = []

    for file in analysis:

        for algo in file["algorithms"]:

            name = algo["name"]

            readiness = ALGORITHM_READINESS.get(name, 50)

            scores.append(readiness)

    if len(scores) == 0:

        return 100

    return round(sum(scores) / len(scores))