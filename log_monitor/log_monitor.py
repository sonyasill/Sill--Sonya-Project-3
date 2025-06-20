import json
import re
from datetime import datetime

#Load the Configuration
with open('config.json', 'r') as f:
    config = json.load(f)

log_files = config["log_files"]
rules = config ["rules"]

alerts = []

#Go through each log File
for log_file in log_files:
    try:
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
            line = f.readlines()
    except FileNotFoundError:
        print(f'File not found: {log_file}')
        continue

#Check each line against each rule
for line_number, line in enumerate(lines, 1):
    for rule_name, rule in rules.items():
        if re.search(rule["pattern"], line, re.IGNORECASE):
            alert = f"[{datetime.now()}] {log_file}:{line_number} - {rule['description']}\n--> {line.strip()}\n"
            alerts.append(alert)

#Save alerts to a file
if alerts:
    with open('alerts.log', 'a') as f:
        for alert in alerts:
            f.write(alert + '\n')

print("Log scan complete.")
