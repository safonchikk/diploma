from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
import requests
import tempfile
import logging

from creator_screen import CreatorScreen


class Short(MDBoxLayout):
    def __init__(self, content_id,title,creator_id,avatar,like_count, **kwargs):
        super(Short, self).__init__(**kwargs)
        ...
        #self.ids.video =
        if avatar == "NO":
            self.ids.author_avatar.source ='images/account.png'
        else:
            self.ids.author_avatar.texture = avatar
        self.ids.title.text = title
        self.author_id =creator_id
        self.like_count = like_count
        self.content_id = content_id
        logging.basicConfig(level=logging.DEBUG)
        logging.debug(content_id)
        response = requests.get("https://lifehealther.onrender.com/short/" + str(content_id), stream=True)
        # response = requests.get("https://lifehealther.onrender.com/video/30", stream=True)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
        file_path = temp_file.name


        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                logging.debug("5")
                f.write(chunk)

        # Вставка відео у VideoPlayer
        self.ids.video.source = file_path
        # self.ids.video.source = 'images/cat_video.mp4'

    def open_creator(self):
        sm = MDApp.get_running_app().sm
        sm.screen_history.append(sm.current)
        #sm.add_widget(CreatorScreen(self.author_id))
        #sm.current = 'creator'
