from fastapi import APIRouter

import app.services.upload_service as upload_service

from app.services.recommendation_service import generate_ai_recommendation
from app.services.migration_service import generate_migration_plan

router = APIRouter(
    prefix="/migration",
    tags=["Migration Planner"]
)


@router.get("/")
def migration_plan():

    recommendations = generate_ai_recommendation(
        upload_service.latest_analysis
    )

    plan = generate_migration_plan(recommendations)

    return plan