from kivy.uix.button import Button
from kivy.properties import ObjectProperty


class ShortPreview(Button):
    def __init__(self, content_id,
                 title,
                 author_name,
                 thumbnail,
                 creator_id,
                 author_avatar,
                 like_count, **kwargs):
        super(ShortPreview, self).__init__(**kwargs)
        if author_avatar == "NO":
            self.ids.author_avatar.source = 'images/account.png'
        else:
            self.ids.author_avatar.texture = author_avatar
        self.ids.author_name.text = author_name
        self.ids.thumbnail.texture = thumbnail
        self.ids.title.text = title
        self.content_id = content_id
        self.creator_id = creator_id
        self.like_count = like_count
