import requests
from kivy.uix.screenmanager import Screen
from kivymd.uix.filemanager import MDFileManager
from plyer import filechooser
from kivy.properties import ListProperty
from kivy.utils import platform
from my_screen import MyScreen


class NewVideoScreen(MyScreen):
    def __init__(self, **kwargs):
        super(NewVideoScreen, self).__init__(**kwargs)
        self.selection = ListProperty([])
        self.chosen_video = ''
        self.chosen_thumbnail = ''

    def choose_video(self):
        '''
        Call plyer filechooser API to run a filechooser Activity.
        '''
        filechooser.open_file(on_selection=self.handle_selection_video)


    def handle_selection_video(self, selection):
        '''
        Callback function for handling the selection response from Activity.
        '''
        self.selection = selection
        path = self.selection[0]
        self.chosen_video = path
        self.ids.video_path.text = path


    def choose_thumbnail(self):
        filechooser.open_file(on_selection=self.handle_selection_thumbnail)


    def handle_selection_thumbnail(self, selection):
        self.selection = selection
        path = self.selection[0]
        self.chosen_thumbnail = path
        self.ids.thumbnail_path.text = path


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
        r = requests.post("https://lifehealther.onrender.com/content/create", json=content_data)
        data = {
            "content_id": r.json()["id"],
            "video_name": title,
            "keywords": tags
        }
        r = requests.post("https://lifehealther.onrender.com/video/create", data=data, files=files)
        f.close()
        video_file.close()
