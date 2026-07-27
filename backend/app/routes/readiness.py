from datetime import datetime

from fastapi import APIRouter
from sqlalchemy import text

from app.database.database import SessionLocal

router = APIRouter(
    prefix="/ready",
    tags=["Readiness"]
)


@router.get("")
def readiness_check():

    database_status = "healthy"

    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()

    except Exception:
        database_status = "unhealthy"

    return {
        "status": "ready" if database_status == "healthy" else "not_ready",
        "database": database_status,
        "timestamp": datetime.utcnow().isoformat()
    }