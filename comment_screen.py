from kivy.uix.screenmanager import Screen

from my_screen import MyScreen


class CommentScreen(MyScreen):
    def __init__(self, **kwargs):
        super(CommentScreen, self).__init__(**kwargs)
        self.ids.comments_grid.bind(minimum_height=self.ids.comments_grid.setter('height'))
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))

    def post(self):
        #=self.ids.comment.text
        ...
