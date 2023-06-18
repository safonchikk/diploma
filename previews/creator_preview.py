from kivy.uix.button import Button


class CreatorPreview(Button):
    def __init__(self, name, avatar, **kwargs):
        super(CreatorPreview, self).__init__()
        self.ids.name.text = name
        self.ids.avatar.texture = avatar
