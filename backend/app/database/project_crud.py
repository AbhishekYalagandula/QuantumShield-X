from sqlalchemy.orm import Session

from app.database.models import Project

from sqlalchemy import func


# ==========================================
# CREATE PROJECT
# ==========================================

def create_project(
    db,
    project_name,
    original_filename,
    extracted_path,
    uploaded_by,
    risk_score,
    risk_level,
    detected_algorithms,
    vulnerable_files,
    report_path=None
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
        report_path=report_path,
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

# ==========================================
# PROJECT DETAILS
# ==========================================

def get_project_details(
    db: Session,
    project_id: int
):

    return (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

# ==========================================
# DELETE PROJECT
# ==========================================

def delete_project(
    db: Session,
    project_id: int
):

    project = (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

    if not project:
        return None

    db.delete(project)
    db.commit()

    return project

# ==========================================
# SEARCH PROJECTS
# ==========================================

def search_projects(
    db: Session,
    keyword: str
):

    return (
        db.query(Project)
        .filter(
            (Project.project_name.ilike(f"%{keyword}%")) |
            (Project.original_filename.ilike(f"%{keyword}%")) |
            (Project.uploaded_by.ilike(f"%{keyword}%"))
        )
        .order_by(Project.upload_time.desc())
        .all()
    )

# ==========================================
# FILTER PROJECTS BY RISK
# ==========================================

def filter_projects_by_risk(
    db: Session,
    risk_level: str
):

    return (
        db.query(Project)
        .filter(Project.risk_level == risk_level)
        .order_by(Project.upload_time.desc())
        .all()
    )

# ==========================================
# MARK PROJECT AS FAVORITE
# ==========================================

def mark_project_favorite(
    db: Session,
    project_id: int
):

    project = (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

    if not project:
        return None

    project.favorite = 1

    db.commit()
    db.refresh(project)

    return project


# ==========================================
# REMOVE FAVORITE
# ==========================================

def remove_project_favorite(
    db: Session,
    project_id: int
):

    project = (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

    if not project:
        return None

    project.favorite = 0

    db.commit()
    db.refresh(project)

    return project


# ==========================================
# GET FAVORITE PROJECTS
# ==========================================

def get_favorite_projects(db: Session):

    return (
        db.query(Project)
        .filter(Project.favorite == 1)
        .order_by(Project.upload_time.desc())
        .all()
    )

# ==========================================
# PROJECT TIMELINE
# ==========================================

def get_project_timeline(
    db: Session,
    project_id: int
):

    project = (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )

    return project

# ==========================================
# ENTERPRISE PROJECT STATISTICS
# ==========================================

def get_project_statistics(db: Session):

    total_projects = db.query(Project).count()

    favorite_projects = (
        db.query(Project)
        .filter(Project.favorite == 1)
        .count()
    )

    average_risk = db.query(
        func.avg(Project.risk_score)
    ).scalar() or 0

    highest_risk = db.query(
        func.max(Project.risk_score)
    ).scalar() or 0

    lowest_risk = db.query(
        func.min(Project.risk_score)
    ).scalar() or 0

    total_algorithms = db.query(
        func.sum(Project.detected_algorithms)
    ).scalar() or 0

    total_reports = (
        db.query(Project)
        .filter(Project.report_path != None)
        .count()
    )

    return {

        "total_projects": total_projects,

        "favorite_projects": favorite_projects,

        "average_risk_score": round(average_risk, 2),

        "highest_risk_score": highest_risk,

        "lowest_risk_score": lowest_risk,

        "total_detected_algorithms": total_algorithms,

        "reports_generated": total_reports

    }

# ==========================================
# ENTERPRISE DASHBOARD
# ==========================================

def get_enterprise_dashboard(db: Session):

    statistics = get_project_statistics(db)

    recent_projects = get_all_projects(db)[:5]

    favorites = get_favorite_projects(db)

    return {

        "statistics": statistics,

        "recent_projects": [

            {

                "id": p.id,

                "project_name": p.project_name,

                "risk_score": p.risk_score,

                "risk_level": p.risk_level,

                "upload_time": p.upload_time

            }

            for p in recent_projects

        ],

        "favorite_projects": [

            {

                "id": p.id,

                "project_name": p.project_name,

                "risk_score": p.risk_score,

                "risk_level": p.risk_level

            }

            for p in favorites

        ]

    }