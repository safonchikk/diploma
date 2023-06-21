import requests
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen

from comment import Comment
from my_screen import MyScreen
from kivymd.app import MDApp


class CommentScreen(MyScreen):
    def __init__(self, content_id, **kwargs):
        super(CommentScreen, self).__init__(name='comment', **kwargs)
        self.content_id = content_id
        self.ids.comments_grid.bind(minimum_height=self.ids.comments_grid.setter('height'))
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))
        self.customer_id = MDApp.get_running_app().user
        self.username = requests.get("https://lifehealther.onrender.com/user/" + str(self.customer_id)).json()["username"]
        comments = requests.get("https://lifehealther.onrender.com/comment/" + str(self.content_id)).json()
        if comments:
            for i in comments:
                comment = Comment(author_login=i["username"], text=i["text"], size_hint_y=None,
                                  liked=False, height=dp(100))
                self.ids.comments_grid.add_widget(comment)

    def post(self):
        data = {
            "customer": self.customer_id,
            "content": self.content_id,
            "text": self.ids.comment.text,
            "like_count": 0
        }
        r = requests.post("https://lifehealther.onrender.com/comment/create", json=data)
        comment = Comment(author_login=self.username, text=self.ids.comment.text, size_hint_y=None,
                          liked=False, height=dp(100))
        self.ids.comments_grid.add_widget(comment)
        self.ids.comment.text = ''
