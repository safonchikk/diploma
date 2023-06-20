from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
import requests
import tempfile
import logging

from comment_screen import CommentScreen
from creator_screen import CreatorScreen


class Short(MDBoxLayout):
    def __init__(self, content_id,title,creator_id,avatar,like_count, **kwargs):
        super(Short, self).__init__(**kwargs)
        if avatar == "NO":
            self.ids.author_avatar.source ='images/account.png'
        else:
            self.ids.author_avatar.texture = avatar
        self.ids.title.text = title
        self.author_id =creator_id
        self.like_count = like_count
        self.content_id = content_id
        logging.basicConfig(level=logging.DEBUG)
        response = requests.get("https://lifehealther.onrender.com/short/" + str(content_id), stream=True)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
        file_path = temp_file.name
        self.customer_id = MDApp.get_running_app().user
        self.content_id = content_id
        liked_r = requests.get(
            "https://lifehealther.onrender.com/content_like/" + str(content_id) + "/" + str(self.customer_id))
        if liked_r.status_code == 404:
            self.liked = False
        elif liked_r.status_code == 200:
            self.liked = True
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        self.ids.video.source = file_path

        if self.liked:
            self.ids.like_icon.source = "images/liked.png"

    def open_creator(self):
        sm = MDApp.get_running_app().sm
        sm.screen_history.append(sm.current)
        sm.add_widget(CreatorScreen(self.author_id))
        sm.current = 'creator'

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

    def comment(self):
        sm = MDApp.get_running_app().sm
        sm.screen_history.append(sm.current)
        sm.add_widget(CommentScreen(self.content_id))
        sm.current = 'comment'
        sm.transition.direction = 'up'
