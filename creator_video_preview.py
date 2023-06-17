from kivy.uix.button import Button
from kivy.properties import ObjectProperty


class CreatorVideoPreview(Button):
    def __init__(self, thumbnail, title='Title', **kwargs):
        super(CreatorVideoPreview, self).__init__(**kwargs)
        self.ids.thumbnail.texture = thumbnail
        self.ids.title.text = title

    def delete(self):
        pass