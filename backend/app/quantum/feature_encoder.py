import math

# --------------------------------------
# Base angle for each algorithm
# --------------------------------------

BASE_ANGLES = {

    "RSA": 2.80,
    "ECC": 2.30,
    "ECDSA": 2.30,
    "TLS": 1.60,
    "SHA-1": 2.00,
    "SHA-256": 0.80,
    "SHA-3": 0.40,
    "AES": 0.60,
    "DES": 2.60,
    "MD5": 2.90

}

# --------------------------------------
# Risk adjustment
# --------------------------------------

RISK_WEIGHT = {

    "Critical": 0.50,
    "High": 0.35,
    "Medium": 0.20,
    "Low": 0.05,
    "Safe": 0.00

}

# --------------------------------------
# Encode project into quantum features
# --------------------------------------

def encode_features(analysis):

    features = []

    total_files = len(analysis)

    for file in analysis:

        total_algorithms = len(file["algorithms"])

        for algo in file["algorithms"]:

            name = algo["name"]

            risk = algo["risk"]

            base = BASE_ANGLES.get(name, 1.0)

            risk_adjustment = RISK_WEIGHT.get(risk, 0)

            density = total_algorithms * 0.08

            project_size = total_files * 0.04

            theta = base + risk_adjustment + density + project_size

            theta = theta % (2 * math.pi)

            features.append({

                "algorithm": name,

                "risk": risk,

                "theta": theta

            })

    return features