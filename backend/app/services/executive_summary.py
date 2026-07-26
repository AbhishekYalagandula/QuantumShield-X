def generate_executive_summary(risk_data):
    score = risk_data["score"]
    readiness = risk_data["readiness"]

    if score >= 85:
        return (
            "Critical quantum vulnerabilities were detected. "
            "Immediate migration to Post-Quantum Cryptography is strongly recommended. "
            "Current cryptographic assets are highly vulnerable to future quantum attacks."
        )

    elif score >= 65:
        return (
            "Several quantum-vulnerable algorithms were detected. "
            "Migration planning should begin as soon as possible to improve long-term security."
        )

    elif score >= 40:
        return (
            "The project contains moderate quantum risks. "
            "Updating vulnerable algorithms will significantly improve quantum readiness."
        )

    else:
        return (
            "The project demonstrates good quantum readiness. "
            "Only minor improvements are recommended for complete future-proof security."
        )