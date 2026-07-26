from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.upload_service import save_uploaded_file
from app.auth.permissions import require_roles

from fastapi import Request
from app.services.audit_service import log_action

router = APIRouter()


@router.post("/upload")
async def upload_project(
    request: Request,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(require_roles(["Admin", "Analyst"]))
):
    result = save_uploaded_file(file, db)
    log_action(
    db=db,
    current_user=current_user,
    action="UPLOAD_PROJECT",
    resource=result["filename"],
    ip_address=request.client.host
)
    return result