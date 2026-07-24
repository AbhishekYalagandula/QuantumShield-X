from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)


@router.get("/{filename}")
def download_report(filename: str):

    report_path = os.path.join(
        "app",
        "reports",
        filename
    )

    if not os.path.exists(report_path):
        return {
            "error": "Report not found"
        }

    return FileResponse(
        path=report_path,
        filename=filename,
        media_type="text/plain"
    )