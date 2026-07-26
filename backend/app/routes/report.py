from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import os

from app.database.database import get_db
from app.database.report_crud import (
    get_all_reports,
    get_report,
    delete_report
)

from app.services.report_metadata import get_report_metadata

from app.services.report_analytics import generate_report_analytics

from fastapi import Request
from app.services.audit_service import log_action
from app.auth.current_user import get_current_user

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)

# ==========================================
# DOWNLOAD REPORT USING FILE PATH
# ==========================================

@router.get("/download")
def download_report(
    path: str,
    request: Request,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    if not os.path.exists(path):
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    return FileResponse(
        path,
        media_type="application/pdf",
        filename=os.path.basename(path)
    )

# ==========================================
# REPORT METADATA
# ==========================================

@router.get("/metadata/{project_id}")
def report_metadata(
    project_id: int,
    db: Session = Depends(get_db)
):

    project = get_report(db, project_id)

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return get_report_metadata(project)

# ==========================================
# REPORT HISTORY
# ==========================================

@router.get("/history")
def report_history(
    db: Session = Depends(get_db)
):

    return get_all_reports(db)


# ==========================================
# DOWNLOAD REPORT BY PROJECT ID
# ==========================================

@router.get("/project/{project_id}")
def download_project_report(
    project_id: int,
    db: Session = Depends(get_db)
):

    project = get_report(db, project_id)

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    if not project.report_path:
        raise HTTPException(
            status_code=404,
            detail="Report not generated"
        )

    if not os.path.exists(project.report_path):
        raise HTTPException(
            status_code=404,
            detail="Report file missing"
        )

    log_action(
    db=db,
    current_user=current_user,
    action="DOWNLOAD_REPORT",
    resource=os.path.basename(path),
    ip_address=request.client.host
)

    return FileResponse(
        project.report_path,
        media_type="application/pdf",
        filename=os.path.basename(project.report_path)
    )


# ==========================================
# DELETE REPORT
# ==========================================

@router.delete("/{project_id}")
def remove_report(
    project_id: int,
    db: Session = Depends(get_db)
):

    project = get_report(db, project_id)

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    if project.report_path and os.path.exists(project.report_path):
        os.remove(project.report_path)

    delete_report(db, project_id)

    return {
        "status": "success",
        "message": "Report deleted successfully."
    }

# ==========================================
# REPORT ANALYTICS
# ==========================================

@router.get("/analytics")
def report_analytics(
    db: Session = Depends(get_db)
):

    return generate_report_analytics(db)