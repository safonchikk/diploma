from my_screen import MyScreen


class CreatorScreen(MyScreen):
    def __init__(self, content_id, **kwargs):
        super(CreatorScreen, self).__init__(name='creator', **kwargs)
        #self.ids.info.text =
        #self.ids.login.text =
        #self.ids.avatar.texture =
        ...

    def subscribe(self):
        pass