import os
from sqlalchemy.orm import Session

from app.database.models import Project


def generate_report_analytics(db: Session):

    projects = db.query(Project).all()

    total_reports = 0
    total_size = 0

    high = 0
    medium = 0
    low = 0
    critical = 0

    for project in projects:

        if project.report_path and os.path.exists(project.report_path):

            total_reports += 1

            total_size += os.path.getsize(project.report_path)

        level = (project.risk_level or "").lower()

        if level == "critical":
            critical += 1
        elif level == "high":
            high += 1
        elif level == "medium":
            medium += 1
        else:
            low += 1

    average_size = 0

    if total_reports > 0:
        average_size = round(
            (total_size / total_reports) / 1024,
            2
        )

    return {

        "total_reports": total_reports,

        "total_storage_kb": round(
            total_size / 1024,
            2
        ),

        "average_report_size_kb": average_size,

        "critical_reports": critical,

        "high_reports": high,

        "medium_reports": medium,

        "low_reports": low

    }