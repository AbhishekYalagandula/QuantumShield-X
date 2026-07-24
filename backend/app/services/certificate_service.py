import ssl
import socket

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, ec


def scan_certificate(hostname: str):

    context = ssl.create_default_context()

    with socket.create_connection((hostname, 443), timeout=5) as sock:

        with context.wrap_socket(sock, server_hostname=hostname) as ssock:

            cert = ssock.getpeercert()
            cipher = ssock.cipher()

            # ----------------------------------
            # Detect Certificate Algorithm
            # ----------------------------------

            cert_der = ssock.getpeercert(binary_form=True)

            x509_cert = x509.load_der_x509_certificate(
                cert_der,
                default_backend()
            )

            public_key = x509_cert.public_key()

            if isinstance(public_key, rsa.RSAPublicKey):

                signature_algorithm = "RSA"
                key_size = public_key.key_size

            elif isinstance(public_key, ec.EllipticCurvePublicKey):

                signature_algorithm = "ECDSA"
                key_size = public_key.key_size

            else:

                signature_algorithm = "Unknown"
                key_size = 0

            # ----------------------------------
            # Quantum Risk Analysis
            # ----------------------------------

            if signature_algorithm == "RSA":

                risk = "High"
                quantum_safe = False
                replace_with = "ML-KEM (CRYSTALS-Kyber)"
                priority = "High"

            elif signature_algorithm == "ECDSA":

                risk = "Medium"
                quantum_safe = False
                replace_with = "ML-DSA (Dilithium)"
                priority = "Medium"

            else:

                risk = "Low"
                quantum_safe = True
                replace_with = "Already Quantum Ready"
                priority = "Low"

            # ----------------------------------
            # Return Result
            # ----------------------------------

            return {

                "hostname": hostname,

                "subject": cert.get("subject"),
                "issuer": cert.get("issuer"),

                "valid_from": cert.get("notBefore"),
                "valid_to": cert.get("notAfter"),

                "serial_number": cert.get("serialNumber"),
                "version": cert.get("version"),

                "cipher": cipher[0] if cipher else "Unknown",

                "algorithm": signature_algorithm,
                "key_size": key_size,

                "risk": risk,
                "quantum_safe": quantum_safe,

                "replace_with": replace_with,
                "migration_priority": priority

            }