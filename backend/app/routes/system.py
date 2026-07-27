import platform
from datetime import datetime

from fastapi import APIRouter

from app.core.config import (
    PROJECT_NAME,
    PROJECT_VERSION,
    ENVIRONMENT,
    DEBUG
)

router = APIRouter(
    prefix="/system",
    tags=["System"]
)


@router.get("/info")
def system_info():

    return {

        "project": PROJECT_NAME,

        "version": PROJECT_VERSION,

        "environment": ENVIRONMENT,

        "debug": DEBUG,

        "python_version": platform.python_version(),

        "operating_system": platform.system(),

        "platform": platform.platform(),

        "processor": platform.processor(),

        "server_time": datetime.now()

    }