import json
import csv

data = json.load(open("activity.json"))

with open("messages_api.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["activity"])
    for item in data:
        writer.writerow([item["activity"]])

print("Saved API data")
