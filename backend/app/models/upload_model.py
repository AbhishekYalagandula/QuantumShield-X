from pydantic import BaseModel
from typing import Any


class UploadResponse(BaseModel):
    status: str
    filename: str
    size: str
    scan_results: list[Any]
    message: str