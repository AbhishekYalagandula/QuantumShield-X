import os
import shutil
from datetime import datetime

from app.services.zip_service import extract_zip
from app.scanner.code_scanner import scan_project
from app.services.analyzer_service import analyze_scan_results
from app.services.migration_service import generate_migration_plan
from app.services.report_service import generate_report
from app.services.risk_engine import calculate_quantum_risk

UPLOAD_FOLDER = "app/uploads"
EXTRACT_FOLDER = "app/extracted_projects"


def save_uploaded_file(file):

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(EXTRACT_FOLDER, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{file.filename}"

    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    size = os.path.getsize(file_path)
    size_mb = f"{size / (1024 * 1024):.2f} MB"

    # Default values
    scan_results = []
    analysis = []
    migration_plan = []
    report = ""

    # Only process ZIP files
    if filename.lower().endswith(".zip"):

        project_name = os.path.splitext(filename)[0]
        extract_path = os.path.join(EXTRACT_FOLDER, project_name)

        extract_zip(file_path, extract_path)

        scan_results = scan_project(extract_path)

        analysis = analyze_scan_results(scan_results)

        risk_data = calculate_quantum_risk(analysis)

        migration_plan = generate_migration_plan(analysis)

        report = generate_report(
            filename,
            analysis,
            migration_plan
        )

    return {
    "status": "success",
    "filename": filename,
    "size": size_mb,

    "risk_score": risk_data["score"],
    "detected_algorithms": risk_data["detected"],
    "vulnerable_files": risk_data["files"],

    "analysis": analysis,
    "migration_plan": migration_plan,
    "report": report,

    "message": "Project uploaded, analyzed and report generated successfully."
}