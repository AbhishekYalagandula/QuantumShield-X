import os
import shutil

from app.database.project_crud import (
    delete_project as delete_project_db
)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.database.project_crud import get_project_details
from app.database.project_crud import search_projects
from app.database.project_crud import filter_projects_by_risk
from app.database.project_crud import (
    mark_project_favorite,
    remove_project_favorite,
    get_favorite_projects
)
from app.database.project_crud import get_project_timeline
from app.database.project_crud import get_project_statistics
from app.database.project_crud import get_enterprise_dashboard

from app.auth.permissions import require_roles

from fastapi import Request
from app.services.audit_service import log_action

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)

# ==========================================
# SEARCH PROJECTS
# ==========================================

@router.get("/search/{keyword}")
def search_project(
    keyword: str,
    db: Session = Depends(get_db)
):

    projects = search_projects(
        db,
        keyword
    )

    results = []

    for project in projects:

        results.append({

            "id": project.id,

            "project_name": project.project_name,

            "risk_score": project.risk_score,

            "risk_level": project.risk_level,

            "uploaded_by": project.uploaded_by,

            "upload_time": project.upload_time

        })

    return results

# ==========================================
# FILTER PROJECTS
# ==========================================

@router.get("/filter/{risk_level}")
def filter_projects(
    risk_level: str,
    db: Session = Depends(get_db)
):

    projects = filter_projects_by_risk(
        db,
        risk_level
    )

    results = []

    for project in projects:

        results.append({

            "id": project.id,

            "project_name": project.project_name,

            "risk_score": project.risk_score,

            "risk_level": project.risk_level,

            "uploaded_by": project.uploaded_by,

            "upload_time": project.upload_time

        })

    return results

# ==========================================
# PROJECT TIMELINE
# ==========================================

@router.get("/timeline/{project_id}")
def project_timeline(
    project_id: int,
    db: Session = Depends(get_db)
):

    project = get_project_timeline(
        db,
        project_id
    )

    if not project:

        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return {

        "project": project.project_name,

        "timeline": [

            {
                "step": "Project Uploaded",
                "time": project.upload_time
            },

            {
                "step": "Source Code Scanned",
                "time": project.upload_time
            },

            {
                "step": "Quantum Risk Analysis Completed",
                "time": project.upload_time
            },

            {
                "step": "QML Prediction Generated",
                "time": project.upload_time
            },

            {
                "step": "AI Recommendation Generated",
                "time": project.upload_time
            },

            {
                "step": "Migration Plan Created",
                "time": project.upload_time
            },

            {
                "step": "Enterprise Report Generated",
                "time": project.upload_time
            }

        ]

    }

# ==========================================
# PROJECT STATISTICS
# ==========================================

@router.get("/statistics/overview")
def statistics(
    db: Session = Depends(get_db)
):

    return get_project_statistics(db)

# ==========================================
# ENTERPRISE DASHBOARD
# ==========================================

@router.get("/dashboard/overview")
def enterprise_dashboard(
    db: Session = Depends(get_db)
):

    return get_enterprise_dashboard(db)


@router.get("/{project_id}")
def project_details(
    project_id: int,
    db: Session = Depends(get_db)
):

    project = get_project_details(
        db,
        project_id
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return {

        "id": project.id,

        "project_name": project.project_name,

        "original_filename": project.original_filename,

        "uploaded_by": project.uploaded_by,

        "risk_score": project.risk_score,

        "risk_level": project.risk_level,

        "detected_algorithms": project.detected_algorithms,

        "vulnerable_files": project.vulnerable_files,

        "report_path": project.report_path,

        "upload_time": project.upload_time

    }

# ==========================================
# DELETE PROJECT
# ==========================================

@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    request: Request,
    db: Session = Depends(get_db),
    current_user=Depends(require_roles(["Admin"]))
):

    project = get_project_details(
        db,
        project_id
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    # ---------------------------------------
    # Delete uploaded ZIP
    # ---------------------------------------

    upload_file = os.path.join(
        "app/uploads",
        project.original_filename
    )

    if os.path.exists(upload_file):
        os.remove(upload_file)

    # ---------------------------------------
    # Delete extracted folder
    # ---------------------------------------

    if os.path.exists(project.extracted_path):
        shutil.rmtree(
            project.extracted_path,
            ignore_errors=True
        )

    # ---------------------------------------
    # Delete report
    # ---------------------------------------

    if project.report_path:

        if os.path.exists(project.report_path):
            os.remove(project.report_path)

    # ---------------------------------------
    # Delete quantum circuit image
    # ---------------------------------------

    circuit_image = os.path.join(
        "app/static/circuits",
        f"{project.project_name}.png"
    )

    if os.path.exists(circuit_image):
        os.remove(circuit_image)

    log_action(
    db=db,
    current_user=current_user,
    action="DELETE_PROJECT",
    resource=project.project_name,
    ip_address=request.client.host
)        

    # ---------------------------------------
    # Delete database record
    # ---------------------------------------

    delete_project_db(
    db,
    project_id
)

    return {

        "status": "success",

        "message": "Project deleted successfully."

    }

# ==========================================
# MARK FAVORITE
# ==========================================

@router.put("/{project_id}/favorite")
def favorite_project(
    project_id: int,
    db: Session = Depends(get_db)
):

    project = mark_project_favorite(
        db,
        project_id
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return {
        "message": "Project marked as favorite."
    }

# ==========================================
# REMOVE FAVORITE
# ==========================================

@router.put("/{project_id}/unfavorite")
def unfavorite_project(
    project_id: int,
    db: Session = Depends(get_db)
):

    project = remove_project_favorite(
        db,
        project_id
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    log_action(
    db=db,
    current_user=current_user,
    action="UNFAVORITE_PROJECT",
    resource=project.project_name,
    ip_address=request.client.host
)

    return {
        "message": "Project removed from favorites."
    }

# ==========================================
# GET FAVORITES
# ==========================================

@router.get("/favorites")
def favorites(
    db: Session = Depends(get_db)
):

    projects = get_favorite_projects(db)

    return [

        {
            "id": project.id,
            "project_name": project.project_name,
            "risk_score": project.risk_score,
            "risk_level": project.risk_level,
            "uploaded_by": project.uploaded_by,
            "upload_time": project.upload_time
        }

        for project in projects

    ]