
doesn't work properly yet-----?? if anyone can help updating yaml lmk 

#  Auto GitHub Commit Bot

This is a fully automated GitHub bot that makes daily commits to your repository — no manual work needed!  
It’s designed to Keep your contribution graph green

# Functionalities #
-  i added customizable commit messages
-  It makes 7 commits per day and 12 on special day (my lucky day is Wednesdays!)
-  I've kept the commit log tidy by trimming it to the last 50 entries
# - In short it just generates random commits #
##  Files Included

| File | Purpose |
|------|---------|
| `autocommit.py` | Generates random commit messages to data.txt |
| `data.txt` | Tracks each commit |
| `.github/workflows/commit.yml` | GitHub Actions workflow |

---

##  How It Works

- **Every day at 3 AM UTC**, GitHub Actions triggers the `autocommit.py` script.
- The script:
  - Adds 7-12 entries in `data.txt`
- The action commits the update with the selected message.
- To keep it clean the log is trimmed to the **last 50 commits only** to keep the file clean.

---
## Days Customization ##
If you want to change the number of days and commit just look into autocommit.py 
It'll surely help you

## Schedule Customization ##

Change this in `.github/workflows/commit.yml` to update the run time:
``` yaml
cron: '0 3 * * *'  # Every day at 3 AM UTC
```
## Fork this repo and Watch your GitHub contribution graph turn green 
👤 Author
Made by Mansoob E Zehra
 Inspired by creativity, caffeine, and laziness 

🛡 License
MIT License – do whatever you want, just keep the bot friendly.
