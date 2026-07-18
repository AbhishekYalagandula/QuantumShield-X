# app/database/crud.py

from sqlalchemy.orm import Session

from app.database.models import Project


def create_project(
    db: Session,
    project_name,
    risk_score,
    risk_level,
    total_findings,
):

    project = Project(
        project_name=project_name,
        risk_score=risk_score,
        risk_level=risk_level,
        total_findings=total_findings,
        status="Completed",
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return project


def get_projects(db: Session):

    return db.query(Project).order_by(Project.id.desc()).all()