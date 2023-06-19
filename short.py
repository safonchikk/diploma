from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout


class Short(MDBoxLayout):
    def __init__(self, content_id, **kwargs):
        self.h = dp(800)
        super(Short, self).__init__(**kwargs)
        ...
        #self.ids.video =
        self.height = dp(800)
        self.ids.video.source = 'images/cat_video.mp4'

