'''
Data access functions for the website.
'''

import json


def get_status():
    with open("static/ryan_status.json", "r") as f:
        return json.load(f);


def update_status(new_status):
    with open("static/ryan_status.json", "w") as f:
        return json.dump(new_status, f)
