from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader

from app.core.config import API_KEY, API_KEY_NAME

api_key_header = APIKeyHeader(
    name=API_KEY_NAME,
    auto_error=False
)


def verify_api_key(
    api_key: str = Security(api_key_header)
):

    if api_key == API_KEY:
        return api_key

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Invalid or missing API Key"
    )