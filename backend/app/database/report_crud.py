from sqlalchemy.orm import Session

from app.database.models import Project


# ==========================================
# GET ALL REPORTS
# ==========================================

def get_all_reports(db: Session):

    projects = (
        db.query(Project)
        .order_by(Project.upload_time.desc())
        .all()
    )

    reports = []

    for project in projects:

        reports.append({

            "project_id": project.id,

            "project_name": project.project_name,

            "risk_level": project.risk_level,

            "risk_score": project.risk_score,

            "report_path": project.report_path,

            "generated_on": project.upload_time

        })

    return reports


# ==========================================
# GET REPORT BY PROJECT ID
# ==========================================

def get_report(db: Session, project_id: int):

    return (

        db.query(Project)

        .filter(Project.id == project_id)

        .first()

    )


# ==========================================
# DELETE REPORT
# ==========================================

def delete_report(db: Session, project_id: int):

    project = get_report(db, project_id)

    if not project:
        return None

    db.delete(project)

    db.commit()

    return project