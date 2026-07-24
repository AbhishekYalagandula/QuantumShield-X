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

# ==========================================
# CREATE DATABASE TABLES
# ==========================================

Base.metadata.create_all(bind=engine)

# ==========================================
# FASTAPI APP
# ==========================================

app = FastAPI(

    title="QuantumShield-X API",

    description="AI Powered Post-Quantum Migration Toolkit",

    version="1.0.0"

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
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)