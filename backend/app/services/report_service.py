import os
import shutil

REPORT_FOLDER = "app/reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)


def generate_report(filename, analysis, migration_plan):

    report_path = os.path.join(
        REPORT_FOLDER,
        filename.replace(".zip", "_report.txt")
    )

    with open(report_path, "w", encoding="utf-8") as report:

        report.write("QuantumShield-X Security Report\n")
        report.write("=" * 70 + "\n\n")

        report.write(f"Project : {filename}\n\n")

        report.write("SCAN RESULTS\n")
        report.write("=" * 70 + "\n\n")

        for file_analysis in analysis:

            report.write(f"File : {file_analysis['file']}\n")
            report.write("-" * 60 + "\n")

            for algo in file_analysis["algorithms"]:

                report.write(
                    f"Algorithm : {algo['name']}\n"
                )

                report.write(
                    f"Risk      : {algo['risk']}\n"
                )

                report.write(
                    f"Recommendation : {algo['recommendation']}\n\n"
                )

            report.write("\n")

        report.write("\n")
        report.write("MIGRATION PLAN\n")
        report.write("=" * 70 + "\n\n")

        for migration in migration_plan:

            report.write(
                f"Algorithm       : {migration['algorithm']}\n"
            )

            report.write(
                f"Replace With    : {migration['replace_with']}\n"
            )

            report.write(
                f"Priority        : {migration['priority']}\n"
            )

            report.write(
                f"Difficulty      : {migration['difficulty']}\n"
            )

            report.write(
                f"Estimated Time  : {migration['estimated_time']}\n"
            )

            report.write(
                f"Status          : {migration['status']}\n"
            )

            report.write("-" * 60 + "\n")

    # Create a copy named latest_report.txt
    latest_report = os.path.join(
        REPORT_FOLDER,
        "latest_report.txt"
    )

    shutil.copy(
        report_path,
        latest_report
    )

    return report_path