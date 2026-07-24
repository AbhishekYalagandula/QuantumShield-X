def generate_xai(analysis):

    explanations = []

    for file_analysis in analysis:

        file_name = file_analysis["file"]

        for algo in file_analysis["algorithms"]:

            algorithm = algo["name"]

            if algorithm == "RSA":

                reason = "RSA relies on Integer Factorization."

                attack = "Shor's Algorithm"

                confidence = "99%"

            elif algorithm in ["ECC", "ECDSA"]:

                reason = "ECC relies on Elliptic Curve Discrete Logarithm."

                attack = "Shor's Algorithm"

                confidence = "98%"

            elif algorithm == "SHA-1":

                reason = "SHA-1 is vulnerable to collision attacks."

                attack = "Collision Attack"

                confidence = "96%"

            elif algorithm == "TLS":

                reason = "Older TLS versions may not support Post-Quantum Cryptography."

                attack = "Future Quantum TLS Attack"

                confidence = "92%"

            elif algorithm == "AES":

                reason = "AES is affected only by Grover's Algorithm. AES-256 remains secure."

                attack = "Grover's Algorithm"

                confidence = "95%"

            else:

                reason = "No known quantum vulnerability."

                attack = "None"

                confidence = "90%"

            explanations.append({

                "file": file_name,

                "algorithm": algorithm,

                "risk": algo["risk"],

                "reason": reason,

                "quantum_attack": attack,

                "recommendation": algo["recommendation"],

                "confidence": confidence

            })

    return explanations