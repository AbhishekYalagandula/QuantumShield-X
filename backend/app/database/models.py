from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True, nullable=False)

    email = Column(String, unique=True, nullable=False)

    password = Column(String, nullable=False)

    role = Column(
        String,
        default="Viewer"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

# ==========================================
# PROJECTS
# ==========================================
class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    project_name = Column(String, nullable=False)

    original_filename = Column(String, nullable=False)

    extracted_path = Column(String, nullable=False)

    uploaded_by = Column(String, nullable=False)

    risk_score = Column(Integer, default=0)

    risk_level = Column(String, default="Low")

    detected_algorithms = Column(String, default="")

    vulnerable_files = Column(Integer, default=0)

    report_path = Column(String, nullable=True)

    favorite = Column(Integer, default=0)

    upload_time = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

# ==========================================
# AUDIT LOGS
# ==========================================

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, nullable=False)

    email = Column(String, nullable=False)

    role = Column(String, nullable=False)

    action = Column(String, nullable=False)

    resource = Column(String, nullable=True)

    ip_address = Column(String, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )