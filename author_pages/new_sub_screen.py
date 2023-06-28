import requests
from kivy.uix.screenmanager import Screen

from my_screen import MyScreen
from kivymd.app import MDApp


class NewSubScreen(MyScreen):
    def publish(self):
        creator_id = MDApp.get_running_app().user
        name = self.ids.name.text
        description = self.ids.description.text
        price = self.ids.price.text
        data = {
            "creator": int(creator_id),
            'name': name,
            'price': int(price)
        }
        r = requests.post("https://lifehealther.onrender.com/sponsor_tier/create", json=data)
        data = {
            "sponsor_tier_id": r.json()["id"],
            "info": description
        }
        r = requests.post("https://lifehealther.onrender.com/sponsor_tier/mongo/create", json=data)
