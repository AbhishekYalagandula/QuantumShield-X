import platform
from datetime import datetime

from app.core.config import (
    PROJECT_NAME,
    PROJECT_VERSION,
    ENVIRONMENT,
    DEBUG
)


def print_startup_banner():

    print("\n")

    print("=" * 60)
    print("🚀 QuantumShield-X Enterprise Server Started")
    print("=" * 60)

    print(f"Project        : {PROJECT_NAME}")
    print(f"Version        : {PROJECT_VERSION}")
    print(f"Environment    : {ENVIRONMENT}")
    print(f"Debug Mode     : {DEBUG}")

    print(f"Python Version : {platform.python_version()}")
    print(f"Operating Sys  : {platform.system()}")

    print(f"Startup Time   : {datetime.now()}")

    print("=" * 60)
    print("✅ API Ready")
    print("=" * 60)
    print()