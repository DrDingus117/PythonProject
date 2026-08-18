# 1: Read CSV
import csv
import statistics
import json

# 2: Handle Errors
try:
    with open("sample-superstore.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        values = []

        for row in reader:
            values.append(float(row["Sales"]))
            print(row)

except FileNotFoundError:
    print("CSV file not found.")

# 3: Compute Statistics
results = {
    "minimum": min(values),
    "mean": statistics.mean(values),
    "maximum": max(values)
}

# 4: Write to JSON
with open("results.json", "w") as file:
    json.dump(results, file)

# 5: Verify in Terminal
print(results)