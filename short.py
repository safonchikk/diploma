from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout


class Short(MDBoxLayout):
    def __init__(self, content_id, **kwargs):
        super(Short, self).__init__(**kwargs)
        ...
        #self.ids.video =
        self.ids.video.source = 'images/cat_video.mp4'

