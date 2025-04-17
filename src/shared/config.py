import json

with open('config/params.json') as f:
    params = json.load(f)

with open('config/webhook.json') as f:
    webhook = json.load(f)

with open('config/scheduler_params.json') as f:
    scheduler_params = json.load(f)
