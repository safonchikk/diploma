from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from my_screen import MyScreen
from kivy.core.image import Image as CoreImage
import requests
import base64
import os


class CreatorProfileScreen(MyScreen):
    def load_info(self):
        creator_id = MDApp.get_running_app().user
        creator_content = requests.get("https://lifehealther.onrender.com/creator/info/" + str(creator_id)).json()
        creator_mongo = requests.get("https://lifehealther.onrender.com/creator/mongo/" + str(creator_id)).json()
        if creator_mongo["avatar"] == "NO":
            self.ids.avatar.source = 'images/account.png'
        else:
            decoded_bytes = base64.b64decode(creator_mongo["avatar"])
            temp_filename = 'temp_image_avatar' + str(creator_id) + '.png'
            with open(temp_filename, 'wb') as file:
                file.write(decoded_bytes)
            # Створення об'єкта CoreImage з тимчасового зображення
            core_image = CoreImage(temp_filename)
            self.ids.avatar.texture = core_image.texture
            os.remove(temp_filename)
        user = requests.get('https://lifehealther.onrender.com/user/' + str(creator_id)).json()
        self.ids.info.text = creator_content["info"]
        self.ids.login.text = user["username"]
