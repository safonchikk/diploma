from kivy.metrics import dp
from kivy.core.image import Image as CoreImage

from my_screen import MyScreen
from kivymd.app import MDApp

import requests
import base64
import os


class AuthorDiplomasScreen(MyScreen):
    def __init__(self, author_id, **kwargs):
        super(AuthorDiplomasScreen, self).__init__(name='author_diplomas', **kwargs)
        self.ids.diplomas_grid.bind(minimum_height=self.ids.diplomas_grid.setter('height'))
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))
        self.k = 0
        self.load_diplomas()
        self.author_id = author_id

    def load_diplomas(self):
        self.ids.subs_grid.clear_widgets()
        #!!!дивись  аналогічну функцію у diploma_page
        '''
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
                os.remove(temp_filename)'''
