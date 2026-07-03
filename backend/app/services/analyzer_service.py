# app/services/analyzer_service.py

QUANTUM_RECOMMENDATIONS = {
    "RSA": {
        "risk": "High",
        "recommendation": "Replace with CRYSTALS-Kyber"
    },
    "ECC": {
        "risk": "High",
        "recommendation": "Replace with CRYSTALS-Kyber"
    },
    "ECDSA": {
        "risk": "High",
        "recommendation": "Replace with CRYSTALS-Dilithium"
    },
    "DSA": {
        "risk": "High",
        "recommendation": "Replace with CRYSTALS-Dilithium"
    },
    "SHA-1": {
        "risk": "Medium",
        "recommendation": "Replace with SHA-256 or SHA-3"
    },
    "SHA-256": {
        "risk": "Low",
        "recommendation": "Safe for now"
    },
    "SHA-3": {
        "risk": "Low",
        "recommendation": "Recommended"
    },
    "AES": {
        "risk": "Low",
        "recommendation": "Use AES-256"
    },
    "TLS": {
        "risk": "Medium",
        "recommendation": "Upgrade to PQC-enabled TLS"
    }
}


def analyze_scan_results(scan_results):
    """
    Converts detected algorithms into
    quantum security recommendations.
    """

    analysis = []

    for result in scan_results:

        file_analysis = {
            "file": result["file"],
            "algorithms": []
        }

        for algorithm in result["algorithms"]:

            if algorithm in QUANTUM_RECOMMENDATIONS:

                info = QUANTUM_RECOMMENDATIONS[algorithm]

                file_analysis["algorithms"].append({
                    "name": algorithm,
                    "risk": info["risk"],
                    "recommendation": info["recommendation"]
                })

        analysis.append(file_analysis)

    return analysis