from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.upload import router as upload_router
from app.routes.auth import router as auth_router

from app.database.database import engine
from app.database.models import Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="QuantumShield-X API",
    description="AI Powered Post-Quantum Migration Toolkit",
    version="1.0.0",
)

# ==========================
# CORS Configuration
# ==========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
# Routers
# ==========================
app.include_router(auth_router)
app.include_router(upload_router)

# ==========================
# Home Route
# ==========================
@app.get("/")
def home():
    return {
        "message": "Welcome to QuantumShield-X 🚀"
    }