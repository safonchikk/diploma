from kivy.metrics import dp
from kivy.uix.screenmanager import Screen

from comment import Comment
from my_screen import MyScreen


class CommentScreen(MyScreen):
    def __init__(self, content_id, **kwargs):
        super(CommentScreen, self).__init__(name='comment', **kwargs)
        self.ids.comments_grid.bind(minimum_height=self.ids.comments_grid.setter('height'))
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))

    def post(self):
        #=self.ids.comment.text
        comment = Comment(author_login='You', text=self.ids.comment.text, size_hint_y=None)
        self.ids.comments_grid.add_widget(comment)
        self.ids.comment.text = ''
        ...
