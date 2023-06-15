import requests
from kivy.uix.screenmanager import Screen
from kivymd.uix.filemanager import MDFileManager


class NewVideoScreen(Screen):
    def __init__(self, **kwargs):
        super(NewVideoScreen, self).__init__(**kwargs)
        self.chosen_video = ''
        self.chosen_thumbnail = ''
        self.video_file_manager = MDFileManager(
            select_path=self.select_video_path,
            exit_manager=self.exit_manager
        )
        self.thumbnail_file_manager = MDFileManager(
            select_path=self.select_thumbnail_path,
            exit_manager=self.exit_manager
        )

    def open_manager(self, file_manager):
        file_manager.show('\\Games')

    def exit_manager(self, file_manager):
        file_manager.close()

    def select_video_path(self, path):
        self.chosen_video = path
        self.ids.video_path.text = path
        self.exit_manager(self.video_file_manager)

    def select_thumbnail_path(self, path):
        self.chosen_thumbnail = path
        self.ids.thumbnail_path.text = path
        self.exit_manager(self.thumbnail_file_manager)

    def publish(self):
        title = self.ids.title.text
        tags = self.ids.tags.text
        video_path = self.chosen_video
        thumbnail_path = self.chosen_thumbnail
        files = {}
        video_file = open(video_path, 'rb')
        files['video'] = video_file
        f = open(thumbnail_path, 'rb')
        files['preview'] = f
        content_data = {
            "creator": 14,
            "content_type": "video",
            "like_count": 0,
            "is_paid": False
        }
        r = requests.post("http://127.0.0.1:8000/content/create", json=content_data)
        data = {
            "content_id": r.json()["id"],
            "video_name": title,
            "keywords": tags
        }
        r = requests.post("http://127.0.0.1:8000/video/create", data=data, files=files)
        f.close()
        video_file.close()
