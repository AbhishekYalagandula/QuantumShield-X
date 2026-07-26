import os
from datetime import datetime


def get_report_metadata(project):

    if not project.report_path:
        return None

    if not os.path.exists(project.report_path):
        return {
            "status": "Missing",
            "report_name": None,
            "file_size_kb": 0,
            "generated_time": project.upload_time
        }

    file_size = os.path.getsize(project.report_path) / 1024

    modified_time = datetime.fromtimestamp(
        os.path.getmtime(project.report_path)
    )

    return {

        "status": "Available",

        "report_name": os.path.basename(project.report_path),

        "file_size_kb": round(file_size, 2),

        "generated_time": modified_time.strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "risk_level": project.risk_level,

        "risk_score": project.risk_score,

        "project_name": project.project_name

    }