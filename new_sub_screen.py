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
        '''data = {
            "creator": int(creator_id),
            'content_type': "article",
            'like_count': 0,
            'is_paid': False
        }
        r = requests.post("https://lifehealther.onrender.com/content/create", json=data)
        data = {
            "content_id": r.json()["id"],
            "article_name": headline,
            "text": article_text,
            "keywords": tags

        }
        r = requests.post("https://lifehealther.onrender.com/article/create", json=data)'''
