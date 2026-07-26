def generate_final_recommendation(risk_level):

    if risk_level == "Critical":

        return (
            "The uploaded project contains highly vulnerable cryptographic "
            "algorithms that can be broken by future quantum computers. "
            "Immediate migration to NIST-approved Post Quantum Cryptography "
            "(ML-KEM and ML-DSA) is strongly recommended."
        )

    elif risk_level == "High":

        return (
            "The uploaded project contains several quantum-vulnerable "
            "algorithms. Migration planning should begin immediately to "
            "avoid future security risks."
        )

    elif risk_level == "Medium":

        return (
            "The project contains partially quantum-safe cryptography. "
            "Upgrading remaining vulnerable algorithms is recommended."
        )

    else:

        return (
            "Excellent! The project already uses mostly quantum-resistant "
            "cryptography and is considered Quantum Ready."
        )