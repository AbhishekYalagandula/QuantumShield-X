from fastapi import APIRouter

from app.services import upload_service
from app.services.xai_service import generate_xai

router = APIRouter(
    prefix="/xai",
    tags=["Explainable AI"]
)

@router.get("/")
def get_xai():

    return generate_xai(upload_service.latest_analysis)