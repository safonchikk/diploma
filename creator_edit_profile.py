from kivymd.uix.filemanager import MDFileManager
from kivy.core.image import Image as CoreImage

from my_screen import MyScreen
import requests
import base64
import os


class CreatorEditProfile(MyScreen):
    def __init__(self, **kwargs):
        super(CreatorEditProfile, self).__init__(**kwargs)
        self.chosen_avatar = ''
        self.k = 0
        self.file_manager = MDFileManager(
            select_path=self.select_path,
            exit_manager=self.exit_manager
        )

    #тут завантаж старі теги і аву
    def load_current_info(self):
        creator_content = requests.get("https://lifehealther.onrender.com/creator/info/14").json()
        creator_mongo = requests.get('https://lifehealther.onrender.com/creator/mongo/14').json()
        self.ids.save_button.disabled = True
        if creator_mongo["avatar"] == "no":
            self.ids.new_avatar.source = 'images/account.png'
        else:
            decoded_bytes = base64.b64decode(creator_mongo["avatar"])
            temp_filename = 'temp_image' + str(self.k) + '.png'
            with open(temp_filename, 'wb') as file:
                file.write(decoded_bytes)
            # Створення об'єкта CoreImage з тимчасового зображення
            core_image = CoreImage(temp_filename)
            self.ids.new_avatar.texture = core_image.texture

        self.chosen_avatar = ''
        self.ids.avatar_path.text = ''
        #отут

        self.ids.info.text = creator_content["info"]

    @staticmethod
    def open_manager(file_manager):
        file_manager.show('\\Games')

    @staticmethod
    def exit_manager(file_manager):
        file_manager.close()

    def select_path(self, path):
        self.chosen_avatar = path
        self.ids.avatar_path.text = path
        self.ids.new_avatar.source = path
        self.ids.save_button.disabled = False
        self.exit_manager(self.file_manager)

    def save_avatar(self):
        avatar_path = self.chosen_avatar
        files = {}
        f = open(avatar_path, 'rb')
        files['avatar'] = f
        r = requests.put("https://lifehealther.onrender.com/creator/update/avatar/14", files=files)
        f.close()


    def save_info(self):
        info = self.ids.info.text
        data = {
            "info": info
        }
        requests.put("https://lifehealther.onrender.com/creator/14/update", data=data )

