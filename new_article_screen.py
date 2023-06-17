import requests
from kivy.uix.screenmanager import Screen

from my_screen import MyScreen


class NewArticleScreen(MyScreen):
    def publish(self):
        headline = self.ids.headline.text
        article_text = self.ids.article_text.text
        tags = self.ids.tags.text
        data = {
            "creator": 19,
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
        r = requests.post("https://lifehealther.onrender.com/article/create", json=data)
