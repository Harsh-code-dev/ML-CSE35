import csv
import random
import time

activities = ["walking", "sitting", "standing"]

def generate_sensor_values(activity):
    if activity == "walking":
        return random.uniform(1.0, 2.0), random.uniform(0.9, 1.5), random.uniform(1.2, 2.2)
    elif activity == "sitting":
        return random.uniform(0.1, 0.3), random.uniform(0.1, 0.2), random.uniform(0.1, 0.3)
    else:  # standing
        return random.uniform(0.3, 0.5), random.uniform(0.2, 0.4), random.uniform(0.3, 0.6)

with open("sensor_activity.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "ax", "ay", "az", "activity"])

    for i in range(10):  # 10 sample readings
        activity = random.choice(activities)
        ax, ay, az = generate_sensor_values(activity)
        writer.writerow([time.time(), ax, ay, az, activity])

print("Generated sensor data")
