import datetime
import time
import random

filename = "data.txt"
today = datetime.datetime.now()
day_of_week = today.strftime('%A')

commit_count = 5 if day_of_week == "Wednesday" else 1  # at least 1

for i in range(commit_count):
    with open(filename, "a") as f:
        f.write(f"\nAuto commit #{i+1} on {today.strftime('%Y-%m-%d %H:%M:%S')}")

    # Optional: add delay if multiple commits
    time.sleep(random.uniform(0.2, 0.5))

# Trim file to last 50 lines to avoid bloating
with open(filename, "r") as f:
    lines = f.readlines()
with open(filename, "w") as f:
    f.writelines(lines[-50:])
