import os
import shutil
from datetime import datetime

from app.services.zip_service import extract_zip
from app.scanner.code_scanner import scan_project
from app.services.analyzer_service import analyze_scan_results
from app.services.migration_service import generate_migration_plan
from app.services.report_service import generate_report

UPLOAD_FOLDER = "app/uploads"
EXTRACT_FOLDER = "app/extracted_projects"


def save_uploaded_file(file):
    # Create uploads folder if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # Generate unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{file.filename}"

    # Full file path
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Get file size in MB
    size = os.path.getsize(file_path)
    size_mb = f"{size / (1024 * 1024):.2f} MB"

    scan_results = []

    # If uploaded file is a ZIP, extract and scan it
    if filename.lower().endswith(".zip"):

        project_name = os.path.splitext(filename)[0]

        extract_path = os.path.join(EXTRACT_FOLDER, project_name)

        extract_zip(file_path, extract_path)

        scan_results = scan_project(extract_path)
        analysis = analyze_scan_results(scan_results)
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
    "analysis": analysis,
    "migration_plan": migration_plan,
    "report": report,
    "message": "Project uploaded, analyzed and report generated successfully."
}