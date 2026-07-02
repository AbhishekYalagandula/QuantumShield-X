# app/scanner/crypto_detector.py

CRYPTO_PATTERNS = {
    "RSA": [
        "RSA",
        "RSA_generate_key",
        "RSA_public_encrypt",
        "RSA_private_decrypt",
        'KeyPairGenerator.getInstance("RSA")'
    ],

    "ECC": [
        "ECC",
        "EC_KEY",
        "EllipticCurve"
    ],

    "ECDSA": [
        "ECDSA",
        "ECDSA_sign",
        "ECDSA_verify"
    ],

    "DSA": [
        "DSA",
        "DSA_sign"
    ],

    "AES": [
        "AES",
        "AES_encrypt",
        "AES_decrypt"
    ],

    "DES": [
        "DES",
        "DES_encrypt"
    ],

    "SHA-1": [
        "SHA1",
        "SHA-1"
    ],

    "SHA-256": [
        "SHA256",
        "SHA-256"
    ],

    "MD5": [
        "MD5"
    ],

    "TLS": [
        "TLS",
        "SSL"
    ]
}


def detect_algorithms(file_content: str):
    """
    Detect cryptographic algorithms used inside source code.
    """

    detected = set()

    for algorithm, patterns in CRYPTO_PATTERNS.items():

        for pattern in patterns:

            if pattern.lower() in file_content.lower():
                detected.add(algorithm)

    return list(detected)