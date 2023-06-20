from my_screen import MyScreen
from kivy.core.image import Image as CoreImage
import requests
import base64
import os


class ArticleScreen(MyScreen):
    def __init__(self, content_id, **kwargs):
        super(ArticleScreen, self).__init__(name='article', **kwargs)
        url = "https://lifehealther.onrender.com/article/" + str(content_id)
        article_info = requests.get(url)
        article_info = article_info.json()
        content_info = requests.get("https://lifehealther.onrender.com/content/" + str(content_id)).json()
        creator_id = content_info["creator"]
        creator_mongo = requests.get('https://lifehealther.onrender.com/creator/mongo/' + str(creator_id)).json()
        user = requests.get('https://lifehealther.onrender.com/user/' + str(creator_id)).json()
        if creator_mongo["avatar"] == "NO":
            self.ids.author_avatar.source = 'images/account.png'
        else:
            decoded_bytes = base64.b64decode(creator_mongo["avatar"])
            temp_filename = 'article_avatar' + str(content_id) + '.png'
            with open(temp_filename, 'wb') as file:
                file.write(decoded_bytes)
            # Створення об'єкта CoreImage з тимчасового зображення
            core_image = CoreImage(temp_filename)
            self.ids.author_avatar.texture = core_image.texture
            os.remove(temp_filename)
        self.ids.author.text = user["username"]
        self.ids.text.text = article_info["text"]
        self.ids.headline.text = article_info["article_name"]

    def like(self):
        ...
        #self.content_id
