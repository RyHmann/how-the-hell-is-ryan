'''
A class that shows the current climate in New Zealand.
Currently the class sends a Youtube Live url to the front end.
In the future this class will grab an image from my personal Raspberry Pi
'''
class Outlook:
    def __init__(self):
        self.url = "https://www.youtube.com/embed/live_stream?channel=UCzCqciYy1frVneF7l3vIadg"
        self.static_pic = "https://www.journeys.nzta.govt.nz/traffic-and-travel-information/traffic-cameras/wellington/232"