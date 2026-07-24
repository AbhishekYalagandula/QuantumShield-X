from fastapi import APIRouter

from app.services.certificate_service import scan_certificate

router = APIRouter(
    prefix="/certificate",
    tags=["Certificate Scanner"]
)


@router.get("/")
def certificate_scan(hostname: str):

    return scan_certificate(hostname)