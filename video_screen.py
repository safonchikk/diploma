from my_screen import MyScreen
from kivy.core.image import Image as CoreImage
import requests
import base64
import os
import tempfile


class VideoScreen(MyScreen):
    def __init__(self, content_id, **kwargs):
        super(VideoScreen, self).__init__(name='video', **kwargs)
        url = "https://lifehealther.onrender.com/video/info/" + str(content_id)
        video_info = requests.get(url)
        video_info = video_info.json()
        content_info = requests.get("https://lifehealther.onrender.com/content/" + str(content_id)).json()
        creator_id = content_info["creator"]
        creator_mongo = requests.get('https://lifehealther.onrender.com/creator/mongo/' + str(creator_id)).json()
        user = requests.get('https://lifehealther.onrender.com/user/' + str(creator_id)).json()
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

        # Вставка відео у VideoPlayer
        self.ids.video.source = file_path
        self.ids.author.text = user["username"]
        self.ids.title.text = video_info["video_name"]
        ...