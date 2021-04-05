import json

with open('../static/ryan_status.json', 'r') as f:
    ryan_status = json.load(f)["message"]
    print(ryan_status)