# app/services/zip_service.py

import zipfile
import os


def extract_zip(zip_path: str, extract_to: str):
    """
    Extract a ZIP file into the specified folder.
    """

    # Create destination folder if it doesn't exist
    os.makedirs(extract_to, exist_ok=True)

    # Extract ZIP
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)

    return extract_to