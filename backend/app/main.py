from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import engine
from app.database.models import Base

from app.routes.auth import router as auth_router
from app.routes.upload import router as upload_router
from app.routes.dashboard import router as dashboard_router

from app.routes import risk_analyzer
from app.routes import recommendation
from app.routes import migration_planner
from app.routes import report
from app.routes import certificate
from app.routes import xai

from fastapi.staticfiles import StaticFiles

from app.routes.project import router as project_router

from app.routes.audit import router as audit_router

from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.security.rate_limiter import limiter

from starlette.middleware.trustedhost import TrustedHostMiddleware

from app.security.request_logger import RequestLoggingMiddleware

from fastapi import HTTPException

from app.security.exception_handlers import (
    http_exception_handler,
    generic_exception_handler
)

from app.core.config import (
    PROJECT_NAME,
    PROJECT_VERSION,
    DEBUG
)

from app.routes.health import router as health_router

from app.services.startup_service import print_startup_banner

from app.routes.system import router as system_router

from app.routes.readiness import router as readiness_router

# ==========================================
# CREATE DATABASE TABLES
# ==========================================

Base.metadata.create_all(bind=engine)

# ==========================================
# FASTAPI APP
# ==========================================

app = FastAPI(
    title=PROJECT_NAME,
    description="AI Powered Post-Quantum Migration Toolkit",
    version=PROJECT_VERSION,
    debug=DEBUG
)

@app.on_event("startup")
async def startup_event():

    print_startup_banner()

app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)

app.state.limiter = limiter

app.add_middleware(
    SlowAPIMiddleware
)

# ==========================================
# REQUEST LOGGER
# ==========================================

app.add_middleware(
    RequestLoggingMiddleware
)

# ==========================================
# CORS
# ==========================================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)

# ==========================================
# TRUSTED HOSTS
# ==========================================

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=[
        "localhost",
        "127.0.0.1",
        "*.localhost"
    ]
)

# ==========================================
# ROUTERS
# ==========================================

app.include_router(auth_router)

app.include_router(upload_router)

app.include_router(dashboard_router)

app.include_router(risk_analyzer.router)

app.include_router(recommendation.router)

app.include_router(migration_planner.router)

app.include_router(report.router)

app.include_router(certificate.router)

app.include_router(xai.router)

app.include_router(project_router)

app.include_router(audit_router)

app.include_router(health_router)

app.include_router(system_router)

app.include_router(readiness_router)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

# ==========================================
# HOME
# ==========================================

@app.get("/")
def home():

    return {

        "message": "Welcome to QuantumShield-X 🚀",

        "status": "Running",

        "version": "1.0.0"

    }
