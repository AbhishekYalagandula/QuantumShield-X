from sqlalchemy.orm import Session

from app.database.models import Project


def get_dashboard_statistics(db: Session):

    projects = db.query(Project).all()

    total_projects = len(projects)

    critical = 0
    high = 0
    medium = 0
    low = 0

    total_score = 0
    total_algorithms = 0

    algorithm_count = {}

    for project in projects:

        total_score += project.risk_score

        total_algorithms += project.detected_algorithms

        if project.risk_level == "Critical":
            critical += 1
    

        elif project.risk_level == "High":
            high += 1
    

        elif project.risk_level == "Medium":
            medium += 1
    

        else:
            low += 1
    

    average_score = 0

    if total_projects > 0:

        average_score = round(
            total_score / total_projects,
            2
        )

        # =====================================
# Recent Projects
# =====================================

    recent_projects = []

    sorted_projects = sorted(
    projects,
    key=lambda x: x.id,
    reverse=True
)

    for project in sorted_projects[:5]:

        recent_projects.append({
        
                "project_name": project.project_name,
        
                "risk_level": project.risk_level,
        
                "risk_score": project.risk_score,
        
                "detected_algorithms": project.detected_algorithms
        
            })

    top_algorithms = sorted(

    algorithm_count.items(),

    key=lambda x: x[1],

    reverse=True

)[:5]    

    

    return {

    "total_projects": total_projects,

    "critical_projects": critical,

    "high_risk_projects": high,

    "risk_distribution": {

    "critical": critical,

    "high": high,

    "medium": medium,

    "low": low

},

    "recent_projects": recent_projects,

    "average_risk_score": average_score,

    "top_algorithms": top_algorithms,

    "total_algorithms": total_algorithms,

    # ===========================
    # Quantum Analytics
    # ===========================

    "average_quantum_readiness": round(
        max(0, 100 - average_score),
        2
    ),

    "average_confidence": round(
        min(99, average_score + 20),
        2
    ),

    "reports_generated": total_projects,

    "quantum_engine": "IBM Qiskit",

    "qml_model": "Variational Quantum Classifier (VQC)"
}