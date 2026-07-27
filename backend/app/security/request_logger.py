import time
import logging

from starlette.middleware.base import BaseHTTPMiddleware

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("QuantumShield-X")


class RequestLoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        start_time = time.time()

        response = await call_next(request)

        duration = round(
            (time.time() - start_time) * 1000,
            2
        )

        logger.info(

            f"{request.method} "

            f"{request.url.path} "

            f"{response.status_code} "

            f"{duration} ms"

        )

        return response