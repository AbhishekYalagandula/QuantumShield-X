from pydantic import BaseModel

class UploadResponse(BaseModel):
    status: str
    filename: str
    size: str

    risk_score: int
    detected_algorithms: list
    vulnerable_files: int

    analysis: list
    migration_plan: list
    report: str
    message: str