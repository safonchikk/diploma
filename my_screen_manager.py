from kivy.uix.screenmanager import ScreenManager


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_history = []
