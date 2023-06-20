from kivy.uix.button import Button
from kivy.uix.widget import Widget


class Comment(Widget):
    def __init__(self, author_login, text, **kwargs):
        super(Comment, self).__init__(**kwargs)
        self.ids.author_login.text = author_login
        self.ids.text.text = text
