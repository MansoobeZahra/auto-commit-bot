import datetime
import time
import random

filename = "data.txt"
today = datetime.datetime.now()
day_of_week = today.strftime('%A')

commit_count = 5 if day_of_week == "Wednesday" else 2
messages = [
    "Refactored the universe ",
    "Added semicolon. Removed bug.",
    "Making GitHub think I'm productive",
    "Commit number {i+1} for the glory",
    "Life is better with commits {i+1}",
    "Just another commit to keep the streak alive",
    "Auto commit #{i+1} - because why not?",
    "This commit is brought to you by caffeine",
    "Commit #{i+1} - because I can",
    "Automated commit #{i+1} - no humans harmed",
    "Keeping the repo alive with commit #{i+1}",
    "Commit #{i+1} - because the code needs love",
    "Automated commit #{i+1} - just for fun",
    "Commit #{i+1} - because I forgot to do it earlier",
    "Auto commit #{i+1} - making history one line at a time",
    "Commit #{i+1} - because the code is never done",
    "Commit #{i+1} - because I have to keep up appearances",
]

for i in range(commit_count):
    with open(filename, "a") as f:
        f.write(f"\nAuto commit #{i+1} on {today.strftime('%Y-%m-%d %H:%M:%S')}")
    with open("message.txt", "w") as msg:
        msg.write(random.choice(messages).replace("{i+1}", str(i+1)))
    time.sleep(random.uniform(0.5, 1.5))

lines = open(filename).readlines()
# Keep last 50 commits only
open(filename, "w").writelines(lines[-50:])
