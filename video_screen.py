from my_screen import MyScreen


class VideoScreen(MyScreen):
    def __init__(self, content_id, **kwargs):
        super(VideoScreen, self).__init__(name='video', **kwargs)
        #self.ids.author.text =
        #self.ids.title.text =
        #self.ids.author_avatar.texture =
        # self.ids.video =
        ...
