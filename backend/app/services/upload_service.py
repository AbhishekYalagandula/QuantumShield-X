import os
import shutil
from datetime import datetime

from sqlalchemy.orm import Session

from app.services.zip_service import extract_zip
from app.scanner.code_scanner import scan_project
from app.services.analyzer_service import analyze_scan_results
from app.services.risk_engine import calculate_quantum_risk
from app.services.recommendation_service import generate_ai_recommendation
from app.services.migration_service import generate_migration_plan
from app.services.report_service import generate_report

from app.database.project_crud import create_project

from app.benchmark.benchmark_engine import generate_quantum_benchmark

# =====================================================
# STORE LATEST ANALYSIS (used by dashboard/pages)
# =====================================================

latest_analysis = []

UPLOAD_FOLDER = "app/uploads"
EXTRACT_FOLDER = "app/extracted_projects"


# =====================================================
# SAVE & PROCESS UPLOADED PROJECT
# =====================================================

def save_uploaded_file(file, db: Session):

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(EXTRACT_FOLDER, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{file.filename}"

    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    size = os.path.getsize(file_path)
    size_mb = f"{size / (1024 * 1024):.2f} MB"

    scan_results = []
    analysis = []
    recommendations = []
    migration_plan = []
    report = ""

    risk_data = {
        "score": 0,
        "level": "Low",
        "detected": 0,
        "files": 0
    }

    project = None

    # =====================================================
    # PROCESS ONLY ZIP FILES
    # =====================================================

    if filename.lower().endswith(".zip"):

        project_name = os.path.splitext(filename)[0]

        extract_path = os.path.join(
            EXTRACT_FOLDER,
            project_name
        )

        # Extract ZIP
        extract_zip(file_path, extract_path)

        # Scan source code
        scan_results = scan_project(extract_path)

        # Analyze findings
        analysis = analyze_scan_results(scan_results)

        # Save latest analysis
        global latest_analysis
        latest_analysis = analysis

        # Calculate Risk Score
        risk_data = calculate_quantum_risk(
    analysis,
    project_name
)

        # AI Recommendations
        recommendations = generate_ai_recommendation(analysis)

        # Migration Planner
        migration_plan = generate_migration_plan(recommendations)

        benchmark = generate_quantum_benchmark(risk_data)

        risk_data["benchmark"] = benchmark

        report = generate_report(
    project_name,
    analysis,
    migration_plan,
    risk_data
)

        # Save Project into SQLite
        project = create_project(
            db=db,
            project_name=project_name,
            original_filename=filename,
            extracted_path=extract_path,
            uploaded_by="demo@quantumshieldx.com",
            risk_score=risk_data["score"],
            risk_level=risk_data["level"],
            detected_algorithms=risk_data["detected"],
            vulnerable_files=risk_data["files"],
            report_path=report
        )

      

    # =====================================================
    # RESPONSE
    # =====================================================

    return {

        "status": "success",

        "filename": filename,

        "size": size_mb,

        "project_id": project.id if project else None,

        "risk_score": risk_data["score"],

        "risk_level": risk_data["level"],

        "qml_prediction": risk_data["qml_prediction"],

        "confidence": risk_data["confidence"],

        "feature_importance": risk_data["feature_importance"],

        "explanations": risk_data["explanations"],

        "quantum_circuit": risk_data["circuit_image"],

        "detected_algorithms": risk_data["detected"],

        "vulnerable_files": risk_data["files"],

        "analysis": analysis,

        "recommendations": recommendations,

        "migration_plan": migration_plan,

        "benchmark": benchmark,

        "report": report,

        "message": "Project uploaded, analyzed and report generated successfully."

    }