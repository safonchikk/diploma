from kivy.uix.image import Image
from kivy.metrics import dp
from plyer import filechooser
from kivy.properties import ListProperty
from kivy.utils import platform
from kivy.core.image import Image as CoreImage
from kivymd.uix.filemanager import MDFileManager

from my_screen import MyScreen
import requests
import base64
import os


class DiplomaPageScreen(MyScreen):
    def __init__(self, **kwargs):
        if platform == 'android':
            from android.permissions import request_permissions, Permission
            request_permissions([
                Permission.WRITE_EXTERNAL_STORAGE,
                Permission.READ_EXTERNAL_STORAGE,
                Permission.INTERNET,
            ])
        super(DiplomaPageScreen, self).__init__(**kwargs)
        self.ids.diplomas_grid.bind(minimum_height=self.ids.diplomas_grid.setter('height'))
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))
        self.chosen_diploma = ''
        self.k = 0
        self.selection = ListProperty([])
        # self.file_manager = MDFileManager(
        #     select_path=self.select_path,
        #     exit_manager=self.exit_manager
        # )

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
            os.remove(temp_filename)


    def choose(self):
        '''
        Call plyer filechooser API to run a filechooser Activity.
        '''
        filechooser.open_file(on_selection=self.handle_selection)


    def handle_selection(self, selection):
        '''
        Callback function for handling the selection response from Activity.
        '''

        self.selection = selection
        path = self.selection[0]
        self.chosen_diploma = path
        files = {}
        f = open(path, 'rb')
        files['diploma_file'] = f
        data = {
            "creator_id": 14,
        }
        r = requests.post("https://lifehealther.onrender.com/diploma/create", data=data, files=files)
        f.close()
        self.load_diplomas()


