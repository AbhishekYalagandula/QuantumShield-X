# app/scanner/code_scanner.py

import os

from app.scanner.crypto_detector import detect_algorithms


SUPPORTED_EXTENSIONS = (
    ".py",
    ".java",
    ".cpp",
    ".c",
    ".h",
    ".hpp",
    ".js",
    ".ts",
    ".go",
    ".rs"
)


def scan_project(project_path: str):
    """
    Scan all supported source files inside a project.
    """

    results = []

    for root, dirs, files in os.walk(project_path):

        for file in files:

            if file.endswith(SUPPORTED_EXTENSIONS):

                filepath = os.path.join(root, file)

                try:

                    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:

                        content = f.read()

                    detected = detect_algorithms(content)

                    if detected:

                        results.append(
                            {
                                "file": filepath,
                                "algorithms": detected
                            }
                        )

                except Exception as e:

                    print(f"Could not scan {filepath}: {e}")

    return results