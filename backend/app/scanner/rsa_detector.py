import os
import re


RSA_PATTERNS = [
    r"RSA",
    r"RSA2048",
    r"RSA-2048",
    r"RSA1024",
    r"RSA-1024",
]


def detect_rsa(file_path):
    """
    Detects RSA usage inside a source file.
    """

    findings = []

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        for pattern in RSA_PATTERNS:

            if re.search(pattern, content, re.IGNORECASE):

                findings.append({
                    "type": "RSA",
                    "severity": "High",
                    "algorithm": pattern,
                    "file": os.path.basename(file_path),
                    "recommendation": "Replace RSA with CRYSTALS-Kyber (ML-KEM)."
                })

    except Exception:
        pass

    return findings