from fastapi import FastAPI
from app.routes.upload import router as upload_router

app = FastAPI(
    title="QuantumShield-X API",
    description="AI Powered Post-Quantum Migration Toolkit",
    version="1.0.0"
)

app.include_router(upload_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to QuantumShield-X 🚀"
    }