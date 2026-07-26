from app.quantum.feature_encoder import encode_features
from app.quantum.quantum_circuit import build_quantum_circuit
from app.quantum.quantum_classifier import execute_quantum_circuit
from app.services.quantum_metadata import generate_quantum_metadata


def quantum_risk_analysis(
    analysis,
    project_name
):
    """
    Complete Quantum Pipeline
    """

    # =====================================
    # STEP 1 - Encode Features
    # =====================================

    features = encode_features(analysis)

    print("\n========== QUANTUM FEATURES ==========")

    for feature in features:
        print(feature)

    print("======================================\n")

    # =====================================
    # STEP 2 - Build Quantum Circuit
    # =====================================

    circuit, image_path = build_quantum_circuit(
    features,
    filename=project_name
)

    # =====================================
    # STEP 3 - Execute Circuit
    # =====================================

    counts, execution_time = execute_quantum_circuit(circuit)

    print("\n========== QUANTUM COUNTS ==========")
    print(counts)
    print("====================================\n")

    metadata = generate_quantum_metadata(
    circuit,
    execution_time
)

    print("\n========== QUANTUM METADATA ==========")

    for key, value in metadata.items():
        print(f"{key}: {value}")
    

    print("======================================\n")

    # =====================================
    # STEP 4 - Calculate Quantum Risk Score
    # =====================================

    total_shots = sum(counts.values())

    total_ones = 0

    for state, count in counts.items():
        total_ones += state.count("1") * count

    max_possible = len(features) * total_shots

    if max_possible == 0:
        score = 0
    else:
        score = int((total_ones / max_possible) * 100)

    # =====================================
    # STEP 5 - Determine Risk Level
    # =====================================

    if score >= 80:
        level = "Critical"

    elif score >= 60:
        level = "High"

    elif score >= 40:
        level = "Medium"

    elif score >= 20:
        level = "Low"

    else:
        level = "Safe"

    # =====================================
    # STEP 6 - Return Result
    # =====================================

    return {
    "score": score,
    "level": level,
    "counts": counts,
    "features": features,
    "circuit_image": image_path,
    "metadata": metadata
}