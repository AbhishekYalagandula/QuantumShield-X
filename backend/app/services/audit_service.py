from sqlalchemy.orm import Session

from app.database.audit_crud import create_audit_log


def log_action(
    db: Session,
    current_user,
    action: str,
    resource: str = "",
    ip_address: str = ""
):

    create_audit_log(
        db=db,
        username=current_user.username,
        email=current_user.email,
        role=current_user.role,
        action=action,
        resource=resource,
        ip_address=ip_address
    )