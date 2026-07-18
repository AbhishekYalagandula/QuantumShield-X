import os

REPORT_FOLDER = "app/reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)


def generate_report(filename, analysis, migration_plan):

    report_path = os.path.join(
        REPORT_FOLDER,
        filename.replace(".zip", "_report.txt")
    )

    with open(report_path, "w", encoding="utf-8") as report:

        report.write("QuantumShield-X Security Report\n")
        report.write("=" * 60 + "\n\n")

        report.write(f"Project : {filename}\n\n")

        for file_analysis in analysis:

            report.write(f"File : {file_analysis['file']}\n")

            report.write("-" * 50 + "\n")

            for algo in file_analysis["algorithms"]:

                report.write(
                    f"{algo['name']} | Risk: {algo['risk']} | Recommendation: {algo['recommendation']}\n"
                )

            report.write("\n")

        report.write("\nMigration Plan\n")
        report.write("=" * 60 + "\n\n")

        for file_plan in migration_plan:

            report.write(f"File : {file_plan['file']}\n")

            for migration in file_plan["migrations"]:

                report.write(
                    f"{migration['algorithm']}  -->  {migration['replace_with']}\n"
                )

            report.write("\n")

    return report_path