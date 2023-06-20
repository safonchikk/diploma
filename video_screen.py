from kivymd.app import MDApp

from creator_screen import CreatorScreen
from my_screen import MyScreen
from kivy.core.image import Image as CoreImage
import requests
import base64
import os
import tempfile


class VideoScreen(MyScreen):
    def __init__(self, content_id, **kwargs):
        super(VideoScreen, self).__init__(name='video', **kwargs)
        self.customer_id = MDApp.get_running_app().user
        self.content_id = content_id
        url = "https://lifehealther.onrender.com/video/info/" + str(content_id)
        video_info = requests.get(url)
        video_info = video_info.json()
        content_info = requests.get("https://lifehealther.onrender.com/content/" + str(content_id)).json()
        creator_id = content_info["creator"]
        creator_mongo = requests.get('https://lifehealther.onrender.com/creator/mongo/' + str(creator_id)).json()
        user = requests.get('https://lifehealther.onrender.com/user/' + str(creator_id)).json()
        liked_r = requests.get(
            "https://lifehealther.onrender.com/content_like/" + str(content_id) + "/" + str(self.customer_id))
        if liked_r.status_code == 404:
            self.liked = False
        elif liked_r.status_code == 200:
            self.liked = True
        if creator_mongo["avatar"] == "NO":
            self.ids.author_avatar.source = 'images/account.png'
        else:
            decoded_bytes = base64.b64decode(creator_mongo["avatar"])
            temp_filename = 'video_avatar' + str(content_id) + '.png'
            with open(temp_filename, 'wb') as file:
                file.write(decoded_bytes)
            # Створення об'єкта CoreImage з тимчасового зображення
            core_image = CoreImage(temp_filename)
            self.ids.author_avatar.texture = core_image.texture
            os.remove(temp_filename)
        response = requests.get("https://lifehealther.onrender.com/video/" + str(content_id), stream=True)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
        file_path = temp_file.name

        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)

        self.author_id = creator_id
        self.like_count = content_info["like_count"]

        # Вставка відео у VideoPlayer
        self.ids.video.source = file_path
        self.ids.video.state = 'play'
        self.ids.author.text = user["username"]
        self.ids.title.text = video_info["video_name"]

    def like(self):
        if self.liked:
            r = requests.delete(
                "https://lifehealther.onrender.com/content_like/delete/" +
                str(self.content_id) + "/" + str(self.customer_id))
            self.liked = False
            self.like_count -= 1
        else:
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
