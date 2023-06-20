import requests
from kivy.uix.screenmanager import Screen
from kivymd.uix.filemanager import MDFileManager

from my_screen import MyScreen
import requests


class UpdateArticleScreen(MyScreen):
    def __init__(self, content_id, **kwargs):
        super(UpdateArticleScreen, self).__init__(**kwargs)
        self.content_id = content_id
        url = "https://lifehealther.onrender.com/article/" + str(content_id)
        data = requests.get(url).json()
        keywords = data["keywords"]
        keywords_text = ""
        for keyword in keywords:
            keywords_text += keyword + ","
        keywords_text = keywords_text[:-1]
        self.ids.headline.text = data["article_name"]
        self.ids.tags.text = keywords_text

    def publish(self):
        headline = self.ids.headline.text
        tags = self.ids.tags.text
        data = {
            "article_name": headline,
            "keywords": tags
        }
        r = requests.put("https://lifehealther.onrender.com/article/update/"+str(self.content_id), data=data)


