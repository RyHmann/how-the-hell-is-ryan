import json
import models.howsryanda as data_access
'''
A class that gathers any data related to Ryan
'''


class RyanStatus:
    def __init__(self):
        self.current_status = data_access.get_status()["message"]
