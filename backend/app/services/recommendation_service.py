# app/services/recommendation_service.py

def generate_ai_recommendation(analysis):

    recommendations = []

    for file in analysis:

        for algo in file["algorithms"]:

            name = algo["name"]

            if name == "RSA":
                recommendations.append({
                    "algorithm": "RSA",
                    "replace_with": "ML-KEM (CRYSTALS-Kyber)",
                    "priority": "High",
                    "difficulty": "Medium"
                })

            elif name in ["ECC", "ECDSA"]:
                recommendations.append({
                    "algorithm": name,
                    "replace_with": "ML-DSA (Dilithium)",
                    "priority": "High",
                    "difficulty": "Medium"
                })

            elif name == "SHA-1":
                recommendations.append({
                    "algorithm": "SHA-1",
                    "replace_with": "SHA-3",
                    "priority": "Medium",
                    "difficulty": "Easy"
                })

            elif name == "DES":
                recommendations.append({
                    "algorithm": "DES",
                    "replace_with": "AES-256",
                    "priority": "Critical",
                    "difficulty": "Easy"
                })

            elif name == "MD5":
                recommendations.append({
                    "algorithm": "MD5",
                    "replace_with": "SHA-3",
                    "priority": "High",
                    "difficulty": "Easy"
                })

    # Remove duplicates
    unique = []
    seen = set()

    for item in recommendations:

        if item["algorithm"] not in seen:

            unique.append(item)
            seen.add(item["algorithm"])

    return unique