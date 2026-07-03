from pydantic import BaseModel
from typing import Any


class UploadResponse(BaseModel):
    status: str
    filename: str
    size: str
    analysis: list
    migration_plan: list
    report: str
    message: str