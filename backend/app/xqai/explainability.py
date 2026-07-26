def generate_xqai_explanation(analysis, qml_prediction):
    """
    Explainable Quantum AI (XQAI)

    Generates:
    - Feature importance
    - Human-readable explanations
    - Confidence score
    """

    feature_importance = []
    explanations = []

    # -----------------------------
    # Importance mapping
    # -----------------------------

    importance_map = {
        "Critical": 45,
        "High": 30,
        "Medium": 15,
        "Low": 10,
        "Safe": 5
    }

    confidence = 96

    # -----------------------------
    # Build explanations
    # -----------------------------

    for file in analysis:

        for algo in file["algorithms"]:

            name = algo["name"]
            risk = algo["risk"]

            importance = importance_map.get(risk, 5)

            feature_importance.append(
                {
                    "algorithm": name,
                    "importance": importance
                }
            )

            # --------------------------------
            # Human readable explanation
            # --------------------------------

            if name == "RSA":

                explanations.append(
                    "RSA can be broken by Shor's Algorithm on a sufficiently powerful quantum computer."
                )

            elif name == "ECC":

                explanations.append(
                    "ECC is vulnerable to Shor's Algorithm and should migrate to ML-DSA."
                )

            elif name == "SHA-1":

                explanations.append(
                    "SHA-1 is deprecated and should be replaced with SHA-3."
                )

            elif name == "TLS":

                explanations.append(
                    "TLS should migrate toward post-quantum secure implementations."
                )

            elif name == "AES":

                explanations.append(
                    "AES remains relatively quantum-resistant, although AES-256 is recommended."
                )

            else:

                explanations.append(
                    f"{name} requires further quantum security evaluation."
                )

    # -----------------------------
    # Remove duplicate explanations
    # -----------------------------

    explanations = list(dict.fromkeys(explanations))

    # -----------------------------
    # Return XQAI result
    # -----------------------------

    return {

        "qml_prediction": qml_prediction,

        "confidence": confidence,

        "feature_importance": feature_importance,

        "explanations": explanations

    }