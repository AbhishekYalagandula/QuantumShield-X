# app/services/analyzer_service.py

def analyze_scan_results(scan_results):

    analysis = []

    for result in scan_results:

        file_analysis = {
            "file": result["file"],
            "algorithms": []
        }

        for finding in result["algorithms"]:

            file_analysis["algorithms"].append({
                "name": finding["algorithm"],
                "risk": finding["severity"],
                "recommendation": finding["recommendation"]
            })

        analysis.append(file_analysis)

    return analysis