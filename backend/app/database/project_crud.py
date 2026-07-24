from sqlalchemy.orm import Session

from app.database.models import Project


# ==========================================
# CREATE PROJECT
# ==========================================

def create_project(
    db: Session,
    project_name: str,
    original_filename: str,
    extracted_path: str,
    uploaded_by: str,
    risk_score: int,
    risk_level: str,
    detected_algorithms: int,
    vulnerable_files: int,
):

    project = Project(
        project_name=project_name,
        original_filename=original_filename,
        extracted_path=extracted_path,
        uploaded_by=uploaded_by,
        risk_score=risk_score,
        risk_level=risk_level,
        detected_algorithms=detected_algorithms,
        vulnerable_files=vulnerable_files,
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return project


# ==========================================
# GET PROJECT BY ID
# ==========================================

def get_project(
    db: Session,
    project_id: int,
):

    return (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )


# ==========================================
# GET ALL PROJECTS
# ==========================================

def get_all_projects(
    db: Session,
):

    return (
        db.query(Project)
        .order_by(Project.upload_time.desc())
        .all()
    )