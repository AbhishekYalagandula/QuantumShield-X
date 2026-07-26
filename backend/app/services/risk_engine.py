from app.quantum.quantum_engine import quantum_risk_analysis
from app.qml.predictor import predict_project
from app.xqai.explainability import generate_xqai_explanation


def calculate_quantum_risk(analysis, project_name):
    """
    Calculate the overall quantum risk using the QuantumShield-X pipeline.
    """

    # =====================================
    # STEP 1 - Run Quantum Pipeline
    # =====================================

    quantum_result = quantum_risk_analysis(
        analysis,
        project_name
    )

    # =====================================
    # STEP 2 - Quantum Machine Learning Prediction
    # =====================================

    qml_prediction = predict_project(analysis)

    print("\n========== QML Prediction ==========")
    print(qml_prediction)
    print("====================================\n")

    # =====================================
    # STEP 3 - Explainable Quantum AI
    # =====================================

    xqai = generate_xqai_explanation(
        analysis,
        qml_prediction
    )

    # =====================================
    # STEP 4 - Extract Quantum Risk
    # =====================================

    score = quantum_result["score"]
    level = quantum_result["level"]

    # =====================================
    # STEP 5 - Count Algorithms
    # =====================================

    detected_algorithms = set()

    vulnerable_files = len(analysis)

    for file in analysis:

        for algo in file["algorithms"]:

            detected_algorithms.add(algo["name"])

    # =====================================
    # STEP 6 - Return Final Result
    # =====================================

    return {

        "score": score,

        "level": level,

        "detected": len(detected_algorithms),

        "files": vulnerable_files,

        "counts": quantum_result["counts"],

        "features": quantum_result["features"],

        "circuit_image": quantum_result["circuit_image"],

        "metadata": quantum_result["metadata"],

        "qml_prediction": qml_prediction,

        "confidence": xqai["confidence"],

        "feature_importance": xqai["feature_importance"],

        "explanations": xqai["explanations"]

    }