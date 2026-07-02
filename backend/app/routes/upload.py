from fastapi import APIRouter, UploadFile, File
from app.services.upload_service import save_uploaded_file
from app.models.upload_model import UploadResponse

router = APIRouter()


@router.post("/upload", response_model=UploadResponse)
async def upload_project(file: UploadFile = File(...)):
    result = save_uploaded_file(file)
    return result