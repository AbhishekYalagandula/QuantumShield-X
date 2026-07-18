# app/scanner/crypto_detector.py

CRYPTO_PATTERNS = {
    "RSA": {
        "patterns": [
            "RSA",
            "RSA_generate_key",
            "RSA_public_encrypt",
            "RSA_private_decrypt",
            'KeyPairGenerator.getInstance("RSA")'
        ],
        "severity": "Critical",
        "recommendation": "Replace with ML-KEM (CRYSTALS-Kyber)"
    },

    "ECC": {
        "patterns": [
            "ECC",
            "EC_KEY",
            "EllipticCurve"
        ],
        "severity": "High",
        "recommendation": "Replace with ML-DSA"
    },

    "ECDSA": {
        "patterns": [
            "ECDSA",
            "ECDSA_sign",
            "ECDSA_verify"
        ],
        "severity": "High",
        "recommendation": "Replace with ML-DSA"
    },

    "DSA": {
        "patterns": [
            "DSA",
            "DSA_sign"
        ],
        "severity": "Medium",
        "recommendation": "Replace with ML-DSA"
    },

    "AES": {
        "patterns": [
            "AES",
            "AES_encrypt",
            "AES_decrypt"
        ],
        "severity": "Safe",
        "recommendation": "AES-256 is currently quantum resistant except for Grover's quadratic speedup."
    },

    "DES": {
        "patterns": [
            "DES",
            "DES_encrypt"
        ],
        "severity": "Critical",
        "recommendation": "Replace with AES-256"
    },

    "SHA-1": {
        "patterns": [
            "SHA1",
            "SHA-1"
        ],
        "severity": "High",
        "recommendation": "Replace with SHA-256 or SHA-3"
    },

    "SHA-256": {
        "patterns": [
            "SHA256",
            "SHA-256"
        ],
        "severity": "Safe",
        "recommendation": "Currently acceptable"
    },

    "MD5": {
        "patterns": [
            "MD5"
        ],
        "severity": "Critical",
        "recommendation": "Replace with SHA-256"
    },

    "TLS": {
        "patterns": [
            "TLS",
            "SSL"
        ],
        "severity": "Medium",
        "recommendation": "Upgrade to TLS 1.3"
    }
}


def detect_algorithms(file_content: str):

    findings = []

    for algorithm, details in CRYPTO_PATTERNS.items():

        for pattern in details["patterns"]:

            if pattern.lower() in file_content.lower():

                findings.append({
                    "algorithm": algorithm,
                    "severity": details["severity"],
                    "recommendation": details["recommendation"]
                })

                break

    return findings