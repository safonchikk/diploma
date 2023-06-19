from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from video_screen import VideoScreen


class VideoPreview(Button):
    def __init__(self, content_id,
                 title,
                 author_name,
                 thumbnail,
                 creator_id,
                 author_avatar,
                 like_count, **kwargs):
        super(VideoPreview, self).__init__(**kwargs)
        if author_avatar == "NO":
            self.ids.author_avatar.source = 'images/account.png'
        self.ids.author_name.text = author_name
        self.ids.thumbnail.texture = thumbnail
        self.ids.title.text = title
        self.content_id = content_id
        self.creator_id = creator_id
        self.like_count = like_count

    def get_screen(self):
        return VideoScreen(self.content_id)
