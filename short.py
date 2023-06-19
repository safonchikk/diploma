from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout

from creator_screen import CreatorScreen


class Short(MDBoxLayout):
    def __init__(self, content_id, **kwargs):
        super(Short, self).__init__(**kwargs)
        ...
        #self.ids.video =
        #self.ids.author_avatar =
        #self.ids.title =
        #self.author_id =
        self.content_id = content_id
        self.ids.video.source = 'images/cat_video.mp4'

    def open_creator(self):
        sm = MDApp.get_running_app().sm
        sm.screen_history.append(sm.current)
        #sm.add_widget(CreatorScreen(self.author_id))
        #sm.current = 'creator'
