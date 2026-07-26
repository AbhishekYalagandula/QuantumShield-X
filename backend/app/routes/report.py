from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

import os

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)


@router.get("/download")
def download_report(path: str):

    if not os.path.exists(path):

        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    return FileResponse(

        path,

        media_type="application/pdf",

        filename=os.path.basename(path)

    )