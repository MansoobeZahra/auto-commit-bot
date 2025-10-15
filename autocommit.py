import datetime
import time
import random
import os

filename = "data.txt"
today = datetime.datetime.now()
day_of_week = today.strftime('%A')

commit_count = 12 if day_of_week == "Wednesday" else 7  # at least 1

# make surefile exists
if not os.path.exists(filename):
    open(filename, "w").close()
    
for i in range(commit_count):
    with open(filename, "a") as f:
        f.write(f"\nAuto commit #{i+1} on {today.strftime('%Y-%m-%d %H:%M:%S')}")

    # add delay for multiple commits
    time.sleep(random.uniform(0.1, 0.2))

# only last 50 lines 
with open(filename, "r") as f:
    lines = f.readlines()
with open(filename, "w") as f:
    f.writelines(lines[-50:])




