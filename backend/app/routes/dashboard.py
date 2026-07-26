from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.database.dashboard_crud import (
    get_dashboard_summary,
    get_recent_scans,
    get_risk_trend,
    get_complete_dashboard
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary")
def dashboard_summary(
    db: Session = Depends(get_db)
):
    return get_dashboard_summary(db)


@router.get("/recent-scans")
def recent_scans(
    db: Session = Depends(get_db)
):
    return get_recent_scans(db)


@router.get("/risk-trend")
def risk_trend(
    db: Session = Depends(get_db)
):
    return get_risk_trend(db)

@router.get("/")
def complete_dashboard(
    db: Session = Depends(get_db)
):

    return {

        "status": "success",

        "dashboard": get_complete_dashboard(db)

    }