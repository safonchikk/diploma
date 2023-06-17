import requests
from kivy.uix.screenmanager import Screen
from kivymd.uix.filemanager import MDFileManager

from my_screen import MyScreen


class UpdateVideoScreen(MyScreen):

    def publish(self):
        title = self.ids.title.text
        tags = self.ids.tags.text


