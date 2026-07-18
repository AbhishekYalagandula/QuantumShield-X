import os

from app.scanner.rsa_detector import detect_rsa


def run_detectors(file_path):
    """
    Runs every vulnerability detector on a file.
    """

    findings = []

    findings.extend(detect_rsa(file_path))

    # Future detectors
    # findings.extend(detect_ecc(file_path))
    # findings.extend(detect_tls(file_path))
    # findings.extend(detect_sha(file_path))
    # findings.extend(detect_aes(file_path))
    # findings.extend(detect_certificate(file_path))

    return findings