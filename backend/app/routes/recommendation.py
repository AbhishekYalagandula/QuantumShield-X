from fastapi import APIRouter

import app.services.upload_service as upload_service
from app.services.recommendation_service import generate_ai_recommendation

router = APIRouter(
    prefix="/recommendation",
    tags=["AI Recommendation"]
)

@router.get("/")
def recommendation():

    return generate_ai_recommendation(
        upload_service.latest_analysis
    )