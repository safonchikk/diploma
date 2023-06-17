import requests
from kivy.uix.screenmanager import Screen
from kivymd.uix.filemanager import MDFileManager

from my_screen import MyScreen


class UpdateVideoScreen(MyScreen):
    def __init__(self, content_id, **kwargs):
        super(UpdateVideoScreen, self).__init__(**kwargs)

    def publish(self):
        title = self.ids.title.text
        tags = self.ids.tags.text


