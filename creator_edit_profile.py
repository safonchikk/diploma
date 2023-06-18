from kivymd.uix.filemanager import MDFileManager
from kivy.core.image import Image as CoreImage
from plyer import filechooser
from kivy.properties import ListProperty
from kivy.utils import platform

from my_screen import MyScreen
import requests
import base64
import os


class CreatorEditProfile(MyScreen):
    def __init__(self, **kwargs):
        super(CreatorEditProfile, self).__init__(**kwargs)
        self.selection = ListProperty([])
        self.chosen_avatar = ''
        self.k = 0

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
            os.remove(temp_filename)
            self.k += 1

        self.chosen_avatar = ''
        self.ids.avatar_path.text = ''
        #отут

        self.ids.info.text = creator_content["info"]

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
        self.chosen_avatar = path
        self.ids.avatar_path.text = path
        self.ids.new_avatar.source = path
        self.ids.save_button.disabled = False



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

