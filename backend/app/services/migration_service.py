def generate_migration_plan(analysis):
    migration_plan = []

    for file_data in analysis:
        file_plan = {
            "file": file_data["file"],
            "migrations": []
        }

        for algo in file_data["algorithms"]:

            if algo["name"] == "RSA":
                migration = {
                    "algorithm": "RSA",
                    "replace_with": "CRYSTALS-Kyber",
                    "difficulty": "Medium",
                    "estimated_time": "2 Days",
                    "why": "RSA is vulnerable to Shor's Algorithm on quantum computers.",
                    "sample_code": "Use liboqs Kyber API instead of RSA."
                }

            elif algo["name"] == "SHA-1":
                migration = {
                    "algorithm": "SHA-1",
                    "replace_with": "SHA-3",
                    "difficulty": "Easy",
                    "estimated_time": "30 Minutes",
                    "why": "SHA-1 has known collision attacks.",
                    "sample_code": "Replace SHA1() with SHA3_256()."
                }

            elif algo["name"] == "AES":
                migration = {
                    "algorithm": "AES",
                    "replace_with": "AES-256",
                    "difficulty": "Easy",
                    "estimated_time": "15 Minutes",
                    "why": "AES-256 provides stronger security against future attacks.",
                    "sample_code": "Increase AES key size to 256 bits."
                }

            elif algo["name"] == "TLS":
                migration = {
                    "algorithm": "TLS",
                    "replace_with": "PQC-enabled TLS",
                    "difficulty": "Hard",
                    "estimated_time": "5 Days",
                    "why": "Current TLS key exchange may become vulnerable to quantum attacks.",
                    "sample_code": "Use hybrid Kyber + TLS handshake."
                }

            else:
                migration = {
                    "algorithm": algo["name"],
                    "replace_with": "Unknown",
                    "difficulty": "Unknown",
                    "estimated_time": "Unknown",
                    "why": "No migration available.",
                    "sample_code": ""
                }

            file_plan["migrations"].append(migration)

        migration_plan.append(file_plan)

    return migration_plan