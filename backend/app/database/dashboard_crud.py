from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date

from app.database.models import Project

from collections import Counter

# ==========================================
# RECENT SCANS
# ==========================================

def get_recent_scans(db: Session):

    projects = (
        db.query(Project)
        .order_by(Project.upload_time.desc())
        .limit(5)
        .all()
    )

    return [
        {
            "id": project.id,
            "project_name": project.project_name,
            "risk_score": project.risk_score,
            "risk_level": project.risk_level,
            "upload_time": project.upload_time
        }
        for project in projects
    ]


# ==========================================
# DASHBOARD SUMMARY
# ==========================================

def get_dashboard_summary(db: Session):

    # ---------------------------------------
    # Total Projects
    # ---------------------------------------

    total_projects = db.query(Project).count()

    # ---------------------------------------
    # Today's Scans
    # ---------------------------------------

    today_scans = (
        db.query(Project)
        .filter(
            func.date(Project.upload_time) == date.today()
        )
        .count()
    )

    # ---------------------------------------
    # Critical Risk Projects
    # ---------------------------------------

    critical_risks = (
        db.query(Project)
        .filter(Project.risk_level == "Critical")
        .count()
    )

    # ---------------------------------------
    # Average Risk Score
    # ---------------------------------------

    avg_risk = db.query(
        func.avg(Project.risk_score)
    ).scalar()

    if avg_risk is None:
        avg_risk = 0

    # ---------------------------------------
    # PQC Readiness
    # ---------------------------------------

    pqc_ready = max(0, 100 - int(avg_risk))

    # ---------------------------------------
    # Latest Project
    # ---------------------------------------

    latest_project = (
        db.query(Project)
        .order_by(Project.upload_time.desc())
        .first()
    )

    if latest_project:
        risk_score = latest_project.risk_score
        risk_level = latest_project.risk_level
    else:
        risk_score = 0
        risk_level = "Low"

    # ---------------------------------------
    # Return Dashboard Data
    # ---------------------------------------

    return {
    "projects": total_projects,
    "critical": critical_risks,
    "pqc": pqc_ready,
    "today": today_scans,
    "risk_score": risk_score,
    "risk_level": risk_level,

    "migration_progress": 41,
    "vulnerable_algorithms": critical_risks
}


def get_risk_trend(db):

    projects = (
        db.query(Project)
        .order_by(Project.id.asc())
        .all()
    )

    trend = []

    for project in projects:

        trend.append({
           "project": project.project_name.split("_")[-1],
            "risk": project.risk_score
        })

    return trend

# ==========================================
# TOP VULNERABLE ALGORITHMS
# ==========================================

def get_top_algorithms(db: Session):

    projects = db.query(Project).all()

    counter = Counter()

    for project in projects:

        # detected_algorithms should contain values like:
        # RSA,SHA-1,ECC

        if project.detected_algorithms:

            algorithms = project.detected_algorithms.split(",")

            for algo in algorithms:

                algo = algo.strip()

                if algo:

                    counter[algo] += 1

    return [

        {
            "algorithm": name,
            "count": count
        }

        for name, count in counter.most_common()

    ]

# ==========================================
# COMPLETE DASHBOARD
# ==========================================

def get_complete_dashboard(db: Session):

    return {

        "summary": get_dashboard_summary(db),

        "recent_scans": get_recent_scans(db),

        "risk_trend": get_risk_trend(db)

    }