from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.upload_service import save_uploaded_file

router = APIRouter()


@router.post("/upload")
async def upload_project(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    result = save_uploaded_file(file, db)
    return result