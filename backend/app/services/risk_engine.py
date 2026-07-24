from app.quantum.quantum_engine import quantum_risk_analysis


def calculate_quantum_risk(analysis):

    # -----------------------------------
    # Run Quantum Pipeline
    # -----------------------------------

    quantum_result = quantum_risk_analysis(analysis)

    score = quantum_result["score"]

    level = quantum_result["level"]

    # -----------------------------------
    # Count Algorithms
    # -----------------------------------

    detected = set()

    vulnerable_files = len(analysis)

    for file in analysis:

        for algo in file["algorithms"]:

            detected.add(algo["name"])

    return {

        "score": score,

        "level": level,

        "detected": len(detected),

        "files": vulnerable_files,

        # Optional (very useful later)
        "counts": quantum_result["counts"],

        "features": quantum_result["features"]

    }