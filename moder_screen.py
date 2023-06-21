from my_screen import MyScreen


class ModerScreen(MyScreen):
    def __init__(self, **kwargs):
        super(ModerScreen, self).__init__(name='moder', **kwargs)
        self.load_next()

    def load_next(self):
        #self.ids.diploma.texture =
        pass

    def accept(self):
        ...
        self.load_next()

    def reject(self):
        ...
        self.load_next()
