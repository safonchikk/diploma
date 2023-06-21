import requests
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class Comment(Widget):
    def __init__(self, author_login, text, liked, **kwargs):
        super(Comment, self).__init__(**kwargs)
        self.ids.author_login.text = author_login
        self.ids.text.text = text
        self.liked = liked

        if self.liked:
            self.ids.like_icon.source = "images/liked.png"

    def like(self):
        if self.liked:
            self.ids.like_icon.source = "images/like.png"
            self.liked = False
        else:
            self.ids.like_icon.source = "images/liked.png"
            self.liked = True