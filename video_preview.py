from kivy.uix.button import Button
from kivy.properties import ObjectProperty


class VideoPreview(Button):
    def __init__(self, thumbnail, author_avatar='images/account.png',
                 author_name='John Doe',
                 title='Lorem ipsum dolor sit amet.', **kwargs):
        super(VideoPreview, self).__init__(**kwargs)
        self.ids.author_avatar.source = author_avatar
        self.ids.author_name.text = author_name
        self.ids.thumbnail.texture = thumbnail
        self.ids.title.text = title
