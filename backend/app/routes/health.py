from fastapi import APIRouter
from datetime import datetime

from app.core.config import (
    PROJECT_NAME,
    PROJECT_VERSION,
    ENVIRONMENT
)

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("")
def health_check():

    return {
        "status": "healthy",
        "project": PROJECT_NAME,
        "version": PROJECT_VERSION,
        "environment": ENVIRONMENT,
        "timestamp": datetime.utcnow().isoformat()
    }
