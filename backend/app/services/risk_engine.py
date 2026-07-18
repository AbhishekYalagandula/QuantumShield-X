# app/services/risk_engine.py

RISK_POINTS = {

    "RSA": 40,
    "ECC": 30,
    "ECDSA": 30,
    "DSA": 25,

    "TLS": 20,

    "SHA-1": 15,

    "DES": 20,

    "MD5": 25,

    "AES": 5,

    "SHA-256": 0,
    "SHA-3": 0
}


def calculate_quantum_risk(analysis):

    score = 0

    detected = []

    vulnerable_files = len(analysis)

    for file in analysis:

        for algo in file["algorithms"]:

            name = algo["name"]

            detected.append(name)

            score += RISK_POINTS.get(name, 0)

    # Extra weight for project size
    score += min(vulnerable_files * 2, 20)

    # Cap score
    score = min(score, 100)

    # Remove duplicates
    detected = list(set(detected))

    return {
        "score": score,
        "detected": detected,
        "files": vulnerable_files
    }