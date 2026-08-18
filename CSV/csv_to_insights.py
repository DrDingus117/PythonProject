# 1: Read CSV
import csv
import statistics
import json

with open("sample-superstore.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    values = []
    
    for row in reader:
        values.append(float(row["Sales"]))
        print(row)
# 2: Handle Errors

# 3: Compute Statistics

# 4: Write to JSON

# 5: Verify in Terminal