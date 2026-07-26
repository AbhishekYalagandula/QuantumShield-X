from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.audit_crud import get_recent_logs
from app.auth.permissions import require_roles

router = APIRouter(
    prefix="/audit",
    tags=["Audit Logs"]
)


@router.get("/")
def audit_logs(

    db: Session = Depends(get_db),

    current_user=Depends(
        require_roles(["Admin"])
    )

):

    logs = get_recent_logs(db)

    return [

        {
            "username": log.username,
            "email": log.email,
            "role": log.role,
            "action": log.action,
            "resource": log.resource,
            "ip": log.ip_address,
            "time": log.created_at
        }

        for log in logs

    ]