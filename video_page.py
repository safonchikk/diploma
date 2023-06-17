from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivy.core.image import Image as CoreImage

from my_screen import MyScreen
from creator_video_preview import CreatorVideoPreview

import requests
import base64
import os

from video_preview import VideoPreview


class VideoPageScreen(MyScreen):
    def __init__(self, **kwargs):
        super(VideoPageScreen, self).__init__(**kwargs)
        self.ids.videos_grid.bind(minimum_height=self.ids.videos_grid.setter('height'))
        self.load_videos()

    def load_videos(self):
        for i in range(5):
            videos = requests.get("https://lifehealther.onrender.com/video/creator/14")
            for i in videos.json().values():
                url = "https://lifehealther.onrender.com/video/info/" + str(i["id"])
                video_info = requests.get(url)
                video_info = video_info.json()
                decoded_bytes = base64.b64decode(video_info["preview"])
                temp_filename = 'temp_image.png'
                with open(temp_filename, 'wb') as file:
                    file.write(decoded_bytes)

                # Створення об'єкта CoreImage з тимчасового зображення
                core_image = CoreImage(temp_filename)
                url = "https://lifehealther.onrender.com/user/" + str(i["creator"])
                creator_info = requests.get(url)
                creator_info = creator_info.json()
                video_preview = CreatorVideoPreview(size_hint_y=None,
                                             height=dp(300),
                                             thumbnail=core_image.texture,
                                             title=video_info["video_name"]
                                             )
                os.remove(temp_filename)
            self.ids.videos_grid.add_widget(video_preview)
