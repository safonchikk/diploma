from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout

from short import Short


class ShortsPlayer(MDBoxLayout):
    def __init__(self, **kwargs):
        super(ShortsPlayer, self).__init__(**kwargs)
        #self.bind(minimum_height=self.setter('height'))


