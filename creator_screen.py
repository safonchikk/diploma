from author_diplomas import AuthorDiplomasScreen
from author_subs import AuthorSubsScreen
from author_videos import AuthorVideosScreen
from my_screen import MyScreen
from kivy.core.image import Image as CoreImage
import requests
import base64
import os
from kivymd.app import MDApp


class CreatorScreen(MyScreen):
    def __init__(self, creator_id, **kwargs):
        super(CreatorScreen, self).__init__(name='creator', **kwargs)
        self.creator_id = creator_id
        self.load_all_info()


    def load_all_info(self):
        self.customer_id = MDApp.get_running_app().user
        all_info = requests.get(
            "https://lifehealther.onrender.com/load_creator/" + str(self.creator_id) + "/" + str(self.customer_id)).json()
        if all_info["avatar"] == "NO":
            self.ids.avatar.source = 'images/account.png'
        else:
            decoded_bytes = base64.b64decode(all_info["avatar"])
            temp_filename = 'temp_image_avatar_self_screen' + str(self.creator_id) + '.png'
            with open(temp_filename, 'wb') as file:
                file.write(decoded_bytes)
            core_image = CoreImage(temp_filename)
            self.ids.avatar.texture = core_image.texture
            os.remove(temp_filename)
        self.ids.info.text = all_info["info"]
        self.ids.login.text = all_info["username"]
        self.subscribed = all_info["subscribed"]
        self.videos = all_info["videos"]
        self.articles = all_info["articles"]
        self.shorts = all_info["shorts"]
        self.diplomas = all_info["diplomas"]
        self.sponsor_tiers = all_info["sponsor_tiers"]
        avatar = all_info["avatar"]
        if avatar != "NO":
            decoded_bytes = base64.b64decode(avatar)
            temp_filename = 'temp_self_scren_avatar_nnnn_' + str(self.creator_id) + '.png'
            with open(temp_filename, 'wb') as file:
                file.write(decoded_bytes)
            core_image = CoreImage(temp_filename)
            avatar = core_image.texture
            os.remove(temp_filename)
        self.avatar = avatar
        self.info = all_info["info"]
        self.username = all_info["username"]
        if self.subscribed:
            self.ids.subscribe_button.text = 'Unsubscribe'
        else:
            self.ids.subscribe_button.text = 'Subscribe'

    def subscribe(self):
        data = {
            "creator": self.creator_id,
            "customer": self.customer_id
        }
        if self.subscribed:
            self.ids.subscribe_button.text = 'Subscribe'
            r = requests.delete("https://lifehealther.onrender.com/subscription/delete/" + str(self.creator_id) + "/" + str(self.customer_id))
        else:
            self.ids.subscribe_button.text = 'Unsubscribe'
            r = requests.post("https://lifehealther.onrender.com/subscription/create", data)
        self.subscribed = not self.subscribed

    def get_videos_screen(self):
        return AuthorVideosScreen(self.creator_id, self.videos, self.username, self.avatar, self.info)

    def get_subs_screen(self):
        return AuthorSubsScreen(self.creator_id, self.sponsor_tiers)

    def get_diplomas_screen(self):
        return AuthorDiplomasScreen(self.creator_id)
