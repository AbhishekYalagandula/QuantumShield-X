from sqlalchemy.orm import Session

from app.database.models import AuditLog


def create_audit_log(
    db: Session,
    username: str,
    email: str,
    role: str,
    action: str,
    resource: str = "",
    ip_address: str = ""
):

    log = AuditLog(
        username=username,
        email=email,
        role=role,
        action=action,
        resource=resource,
        ip_address=ip_address
    )

    db.add(log)
    db.commit()

    return log


def get_recent_logs(
    db: Session,
    limit: int = 100
):

    return (
        db.query(AuditLog)
        .order_by(AuditLog.created_at.desc())
        .limit(limit)
        .all()
    )