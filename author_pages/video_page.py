from kivy.metrics import dp
from kivy.core.image import Image as CoreImage

from my_screen import MyScreen
from previews.creator_video_preview import CreatorVideoPreview
from author_pages.new_video_screen import NewVideoScreen
from kivymd.app import MDApp

import requests
import base64
import os


class VideoPageScreen(MyScreen):
    def __init__(self, **kwargs):
        super(VideoPageScreen, self).__init__(**kwargs)
        self.ids.videos_grid.bind(minimum_height=self.ids.videos_grid.setter('height'))
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))
        self.k = 0

    def load_videos(self):
        self.ids.videos_grid.clear_widgets()
        creator_id = MDApp.get_running_app().user
        videos = requests.get("https://lifehealther.onrender.com/video/creator/" + str(creator_id))
        if videos.json() != {}:
            for i in videos.json().values():
                url = "https://lifehealther.onrender.com/video/info/" + str(i["id"])
                video_info = requests.get(url)
                video_info = video_info.json()
                decoded_bytes = base64.b64decode(video_info["preview"])
                temp_filename = 'temp_image'+str(self.k)+'.png'
                with open(temp_filename, 'wb') as file:
                    file.write(decoded_bytes)

                # Створення об'єкта CoreImage з тимчасового зображення
                core_image = CoreImage(temp_filename)
                video_preview = CreatorVideoPreview(size_hint_y=None,
                                                    height=dp(300),
                                                    thumbnail=core_image.texture,
                                                    content_id=i["id"],
                                                    title=video_info["video_name"],
                                                    create_upd=self.create_upd
                                                    )
                self.k += 1
                self.ids.videos_grid.add_widget(video_preview)
                os.remove(temp_filename)

    def create_upd(self, upd_screen):
        self.manager.add_widget(upd_screen)
        self.manager.screen_history.append(self.manager.current)
        self.manager.current = 'update_video'

    def create_add(self):
        self.manager.add_widget(NewVideoScreen(name='new_video'))
