from fastapi import APIRouter, UploadFile, File
from app.services.upload_service import save_uploaded_file
import traceback

router = APIRouter()

@router.post("/upload")
async def upload_project(file: UploadFile = File(...)):
    try:
        result = save_uploaded_file(file)
        return result

    except Exception as e:
        print("\n" + "="*80)
        print("UPLOAD ERROR")
        print("="*80)
        traceback.print_exc()
        print("="*80 + "\n")
        raise e