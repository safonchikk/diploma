import requests
from kivy.uix.screenmanager import Screen
from kivymd.uix.filemanager import MDFileManager

from my_screen import MyScreen
import requests


class UpdateVideoScreen(MyScreen):
    def __init__(self, content_id, **kwargs):
        super(UpdateVideoScreen, self).__init__(**kwargs)
        self.content_id = content_id
        url = "https://lifehealther.onrender.com/video/info/" + str(content_id)
        video_data = requests.get(url).json()
        keywords = video_data["keywords"]
        keywords_text = ""
        for keyword in keywords:
            keywords_text += keyword + ","
        keywords_text = keywords_text[:-1]
        self.ids.title.text = video_data["video_name"]
        self.ids.tags.text = keywords_text


    def publish(self):
        title = self.ids.title.text
        tags = self.ids.tags.text
        data = {
            "video_name": title,
            "keywords": tags
        }
        r = requests.put("https://lifehealther.onrender.com/video/update/"+str(self.content_id), data=data)


