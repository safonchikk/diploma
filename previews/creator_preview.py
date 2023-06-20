from kivy.uix.button import Button

from creator_screen import CreatorScreen


class CreatorPreview(Button):
    def __init__(self, name, avatar, author_id, **kwargs):
        super(CreatorPreview, self).__init__(**kwargs)
        self.ids.name.text = name
        self.ids.avatar.texture = avatar
        self.author_id = author_id

    def get_screen(self):
        return CreatorScreen(self.author_id)
