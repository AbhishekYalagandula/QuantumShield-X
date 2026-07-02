from pydantic import BaseModel


class UploadResponse(BaseModel):
    status: str
    filename: str
    size: str
    message: str