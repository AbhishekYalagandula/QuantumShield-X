from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    Request,
    HTTPException
)

from sqlalchemy.orm import Session

import os

from app.database.database import get_db
from app.services.upload_service import save_uploaded_file

from app.auth.permissions import require_roles

from app.services.audit_service import log_action

from app.security.rate_limiter import limiter

router = APIRouter()


@limiter.limit("20/minute")
@router.post("/upload")
async def upload_project(

    request: Request,

    file: UploadFile = File(...),

    db: Session = Depends(get_db),

    current_user=Depends(
        require_roles(["Admin", "Analyst"])
    )

):

    # ==========================================
    # SAFE FILENAME
    # ==========================================

    safe_filename = os.path.basename(file.filename)

    filename = safe_filename.lower()

    # ==========================================
    # ALLOWED FILE TYPES
    # ==========================================

    allowed_extensions = {".zip"}

    if not any(filename.endswith(ext) for ext in allowed_extensions):

        raise HTTPException(
            status_code=400,
            detail="Only ZIP project uploads are allowed."
        )

    # ==========================================
    # FILE SIZE VALIDATION
    # ==========================================

    contents = await file.read()

    MAX_SIZE = 100 * 1024 * 1024   # 100 MB

    if len(contents) == 0:

        raise HTTPException(
            status_code=400,
            detail="Uploaded file is empty."
        )

    if len(contents) > MAX_SIZE:

        raise HTTPException(
            status_code=400,
            detail="Maximum upload size is 100 MB."
        )

    # Reset file pointer
    await file.seek(0)

    # ==========================================
    # SAVE & ANALYZE PROJECT
    # ==========================================

    result = save_uploaded_file(
        file,
        db
    )

    # ==========================================
    # AUDIT LOG
    # ==========================================

    log_action(

        db=db,

        current_user=current_user,

        action="UPLOAD_PROJECT",

        resource=result["filename"],

        ip_address=request.client.host

    )

    # ==========================================
    # RESPONSE
    # ==========================================

    return result