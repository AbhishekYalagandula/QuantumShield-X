# app/services/migration_planner_service.py

def generate_migration_plan(recommendations):

    plan = []

    for item in recommendations:

        if item["algorithm"] == "RSA":

            estimated = "3-5 Days"

        elif item["algorithm"] in ["ECC", "ECDSA"]:

            estimated = "2-4 Days"

        elif item["algorithm"] == "SHA-1":

            estimated = "1 Day"

        elif item["algorithm"] == "DES":

            estimated = "1 Day"

        elif item["algorithm"] == "MD5":

            estimated = "1 Day"

        else:

            estimated = "2 Days"

        plan.append({

            "algorithm": item["algorithm"],

            "replace_with": item["replace_with"],

            "priority": item["priority"],

            "difficulty": item["difficulty"],

            "estimated_time": estimated,

            "status": "Pending"

        })

    return plan