from kivy.metrics import dp
from kivy.core.image import Image as CoreImage
from kivymd.app import MDApp

from my_screen import MyScreen

import requests
import base64
import os

from new_short_screen import NewShortScreen
from previews.short_preview import ShortPreview


class ShortPageScreen(MyScreen):
    def __init__(self, **kwargs):
        super(ShortPageScreen, self).__init__(**kwargs)
        self.ids.videos_grid.bind(minimum_height=self.ids.videos_grid.setter('height'))
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))
        self.k = 0
        #self.load_videos()

    def load_videos(self):
        self.ids.videos_grid.clear_widgets()
        creator_id = MDApp.get_running_app().user
        videos = requests.get("https://lifehealther.onrender.com/short/creator/" + str(creator_id))
        if videos.json() != {}:
            for i in videos.json().values():
                url = "https://lifehealther.onrender.com/short/info/" + str(i["id"])
                video_info = requests.get(url)
                video_info = video_info.json()
                decoded_bytes = base64.b64decode(video_info["preview"])
                temp_filename = 'shor_creator_image'+str(self.k)+'.png'
                with open(temp_filename, 'wb') as file:
                    file.write(decoded_bytes)

                # Створення об'єкта CoreImage з тимчасового зображення
                core_image = CoreImage(temp_filename)
                short_preview = ShortPreview(size_hint_y=None,
                                             height=dp(300),
                                             thumbnail=core_image.texture,
                                             title=video_info["video_name"],
                                             content_id=i["id"]
                                             )
                os.remove(temp_filename)
                self.ids.videos_grid.add_widget(short_preview)

    def create_add(self):
        self.manager.add_widget(NewShortScreen(name='new_short'))
