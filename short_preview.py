from kivy.uix.button import Button
from kivy.properties import ObjectProperty


class ShortPreview(Button):
    def __init__(self, thumbnail,
                 title='Lorem ipsum dolor sit amet.', **kwargs):
        super(ShortPreview, self).__init__(**kwargs)
        self.ids.thumbnail.texture = thumbnail
        self.ids.title.text = title