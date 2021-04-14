from .howsryanda import get_status
'''
A class that gathers any data related to Ryan
'''


class RyanStatus:
    def __init__(self):
        self.current_status = get_status()["message"]
        self.current_projects = get_status()["projects"]
        self.current_reads = get_status()["current_reads"]
