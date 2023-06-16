from kivy.metrics import dp
from kivy.uix.screenmanager import Screen

from my_screen import MyScreen
from video_preview import VideoPreview


class VideoPageScreen(MyScreen):
    def __init__(self, **kwargs):
        super(VideoPageScreen, self).__init__(**kwargs)
        self.ids.videos_grid.bind(minimum_height=self.ids.videos_grid.setter('height'))
        self.load_videos()

    def load_videos(self):
        for i in range(5):
            video_preview = VideoPreview(size_hint_y=None, height=dp(300))
            self.ids.videos_grid.add_widget(video_preview)
