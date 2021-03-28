import json
'''
A class that gathers any data related to Ryan
'''


class RyanStatus:
    def __init__(self):
        self.current_status = self.get_status()

    def get_status(self):
        with open('static/ryan_status.json', 'r') as f:
            ryan_status = json.load(f)["message"]
            return ryan_status
