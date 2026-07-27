import os

from dotenv import load_dotenv

load_dotenv()


SECRET_KEY = os.getenv(
    "SECRET_KEY"
)

ALGORITHM = os.getenv(
    "ALGORITHM",
    "HS256"
)

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES",
        60
    )
)

DATABASE_URL = os.getenv(
    "DATABASE_URL"
)

DEBUG = os.getenv(
    "DEBUG",
    "True"
) == "True"

PROJECT_NAME = os.getenv(
    "PROJECT_NAME"
)

PROJECT_VERSION = os.getenv(
    "PROJECT_VERSION"
)
# ==========================================
# API SECURITY
# ==========================================

API_KEY = os.getenv(
    "API_KEY",
    "QuantumShieldX-2026"
)

API_KEY_NAME = os.getenv(
    "API_KEY_NAME",
    "X-API-Key"
)

# ==========================================
# APPLICATION MODE
# ==========================================

ENVIRONMENT = os.getenv(
    "ENVIRONMENT",
    "development"
)

IS_PRODUCTION = ENVIRONMENT.lower() == "production"

IS_DEVELOPMENT = ENVIRONMENT.lower() == "development"