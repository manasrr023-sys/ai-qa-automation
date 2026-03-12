import csv
import os

def save_results(results):

    os.makedirs("reports", exist_ok=True)

    with open("reports/ai_test_results.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Prompt", "AI Response", "Score", "Status"])

        for row in results:
            writer.writerow(row)