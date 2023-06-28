from kivy.metrics import dp
from kivy.core.image import Image as CoreImage
from kivy.uix.image import Image

from my_screen import MyScreen
from kivymd.app import MDApp

import requests
import base64
import os


class AuthorDiplomasScreen(MyScreen):
    def __init__(self, author_id, diplomas, **kwargs):
        super(AuthorDiplomasScreen, self).__init__(name='author_diplomas', **kwargs)
        self.ids.diplomas_grid.bind(minimum_height=self.ids.diplomas_grid.setter('height'))
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))
        self.k = 0
        self.diplomas = diplomas
        self.load_diplomas()
        self.author_id = author_id

    def load_diplomas(self):
        self.ids.diplomas_grid.clear_widgets()
        if self.diplomas:
            for i in self.diplomas:
                decoded_bytes = base64.b64decode(i["file"])
                temp_filename = 'temp_diploma_self_screen' + str(self.k) + '.png'
                with open(temp_filename, 'wb') as file:
                    file.write(decoded_bytes)
                core_image = CoreImage(temp_filename)
                diploma = Image(size_hint=(1, None))
                diploma.texture = core_image.texture
                diploma.height = dp(200)
                diploma.width = dp(300)
                self.ids.diplomas_grid.add_widget(diploma)
                self.k += 1
                os.remove(temp_filename)