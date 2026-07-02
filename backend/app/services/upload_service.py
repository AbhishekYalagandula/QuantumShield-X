import os
import shutil
from datetime import datetime

UPLOAD_FOLDER = "app/uploads"


def save_uploaded_file(file):
    # Create uploads folder if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    # Generate unique filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{file.filename}"

    # Full file path
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Get file size in MB
    size = os.path.getsize(file_path)
    size_mb = f"{size / (1024 * 1024):.2f} MB"

    return {
        "status": "success",
        "filename": filename,
        "size": size_mb,
        "message": "Project uploaded successfully."
    }