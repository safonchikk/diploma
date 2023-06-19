from my_screen import MyScreen


class ArticleScreen(MyScreen):
    def __init__(self, content_id, **kwargs):
        super(ArticleScreen, self).__init__(name='article', **kwargs)

        ...
