#!/usr/bin/env python3
import json
with open('ex5.json', 'r') as file:
    sample = json.load(file)

for i in sample:
    if i["name"] == "Old Fashioned" and i["type"] == "donut": 
        i["batters"]["batter"].append({"id": "1005", "type": "Tea"})
        break

with open('ex5.json', 'w') as file_write:
    json.dump(sample, file_write, indent=2)
