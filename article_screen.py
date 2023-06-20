from comment_screen import CommentScreen
from creator_screen import CreatorScreen
from my_screen import MyScreen
from kivy.core.image import Image as CoreImage
from kivymd.app import MDApp
import requests
import base64
import os


class ArticleScreen(MyScreen):
    def __init__(self, content_id, **kwargs):
        super(ArticleScreen, self).__init__(name='article', **kwargs)
        self.customer_id = MDApp.get_running_app().user
        url = "https://lifehealther.onrender.com/article/" + str(content_id)
        article_info = requests.get(url)
        article_info = article_info.json()
        content_info = requests.get("https://lifehealther.onrender.com/content/" + str(content_id)).json()
        creator_id = content_info["creator"]
        self.content_id = content_id
        creator_mongo = requests.get('https://lifehealther.onrender.com/creator/mongo/' + str(creator_id)).json()
        user = requests.get('https://lifehealther.onrender.com/user/' + str(creator_id)).json()
        liked_r = requests.get("https://lifehealther.onrender.com/content_like/" + str(content_id) + "/" + str(self.customer_id))
        if liked_r.status_code == 404:
            self.liked = False
        elif liked_r.status_code == 200:
            self.liked = True
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
        self.author_id = creator_id
        self.ids.author.text = user["username"]
        self.ids.text.text = article_info["text"]
        self.ids.headline.text = article_info["article_name"]
        self.like_count = content_info["like_count"]

        if self.liked:
            self.ids.like_icon.source = "images/liked.png"

    def like(self):
        if self.liked:
            self.ids.like_icon.source = "images/like.png"
            r = requests.delete(
                "https://lifehealther.onrender.com/content_like/delete/" +
                str(self.content_id) + "/" + str(self.customer_id))
            self.liked = False
            self.like_count -= 1
        else:
            self.ids.like_icon.source = "images/liked.png"
            data = {
                "content_id": int(self.content_id),
                "customer_id": int(self.customer_id)
            }
            r = requests.post("https://lifehealther.onrender.com/content_like/create", json=data)
            self.liked = True
            self.like_count += 1

    def open_creator(self):
        sm = MDApp.get_running_app().sm
        sm.screen_history.append(sm.current)
        sm.add_widget(CreatorScreen(self.author_id))
        sm.current = 'creator'

    def comment(self):
        sm = MDApp.get_running_app().sm
        sm.screen_history.append(sm.current)
        sm.add_widget(CommentScreen(self.content_id))
        sm.current = 'comment'
        sm.transition.direction = 'up'
