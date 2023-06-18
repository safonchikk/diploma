from kivy.uix.image import Image
from kivy.metrics import dp
from kivy.core.image import Image as CoreImage
from kivymd.uix.filemanager import MDFileManager

from my_screen import MyScreen
import requests
import base64
import os


class DiplomaPageScreen(MyScreen):
    def __init__(self, **kwargs):
        super(DiplomaPageScreen, self).__init__(**kwargs)
        self.ids.diplomas_grid.bind(minimum_height=self.ids.diplomas_grid.setter('height'))
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))
        self.chosen_diploma = ''
        self.k = 0
        self.file_manager = MDFileManager(
            select_path=self.select_path,
            exit_manager=self.exit_manager
        )

    def load_diplomas(self):
        self.ids.diplomas_grid.clear_widgets()
        diplomas = requests.get("https://lifehealther.onrender.com/diploma/creator/get/14")
        for i in diplomas.json().values():
            decoded_bytes = base64.b64decode(i["file"])
            temp_filename = 'temp_diploma' + str(self.k) + '.png'
            with open(temp_filename, 'wb') as file:
                file.write(decoded_bytes)

            # Створення об'єкта CoreImage з тимчасового зображення
            core_image = CoreImage(temp_filename)
            diploma = Image(size_hint=(1, None))
            diploma.texture = core_image.texture
            self.ids.diplomas_grid.add_widget(diploma)
            self.k += 1

    @staticmethod
    def open_manager(file_manager):
        file_manager.show('\\Games')

    def exit_manager(self, file_manager):
        file_manager.close()
        self.load_diplomas()

    def select_path(self, path):
        self.chosen_diploma = path
        files = {}
        f = open(path, 'rb')
        files['diploma_file'] = f
        data = {
            "creator_id": 14,
        }
        r = requests.post("https://lifehealther.onrender.com/diploma/create", data=data, files=files)
        f.close()
        self.exit_manager(self.file_manager)
