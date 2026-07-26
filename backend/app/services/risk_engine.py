from app.quantum.quantum_engine import quantum_risk_analysis

from app.qml.predictor import predict_project

from app.xqai.explainability import generate_xqai_explanation


def calculate_quantum_risk(analysis, project_name):
    """
    Calculate the overall quantum risk using the Qiskit pipeline.
    """

    # -----------------------------------
    # Run Quantum Pipeline
    # -----------------------------------

    quantum_result = quantum_risk_analysis(
        analysis,
        project_name
    )
    # -----------------------------------
# Explainable Quantum AI
# -----------------------------------

    xqai = generate_xqai_explanation(
    analysis,
    quantum_result["qml_prediction"]
)

    # -----------------------------------
# Quantum ML Prediction
# -----------------------------------

    qml_prediction = predict_project(analysis)

    print("\n========== QML Prediction ==========")
    print(qml_prediction)
    print("====================================\n")

    score = quantum_result["score"]
    level = quantum_result["level"]

    # -----------------------------------
    # Count detected algorithms
    # -----------------------------------

    detected = set()

    vulnerable_files = len(analysis)

    for file in analysis:

        for algo in file["algorithms"]:

            detected.add(algo["name"])

    # -----------------------------------
    # Return Result
    # -----------------------------------

    return {

        "score": score,

        "level": level,

        "detected": len(detected),

        "files": vulnerable_files,

        "counts": quantum_result["counts"],

        "features": quantum_result["features"],

        "circuit_image": quantum_result["circuit_image"],

        "qml_prediction": qml_prediction,

        "qml_prediction": xqai["qml_prediction"],

        "confidence": xqai["confidence"],

        "feature_importance": xqai["feature_importance"],

        "explanations": xqai["explanations"]

    }