from kivy.metrics import dp
from kivy.uix.screenmanager import Screen

from article_preview import ArticlePreview
from my_screen import MyScreen


class ArticlePageScreen(MyScreen):
    def __init__(self, **kwargs):
        super(ArticlePageScreen, self).__init__(**kwargs)
        self.ids.articles_grid.bind(minimum_height=self.ids.articles_grid.setter('height'))
        self.load_articles()

    def load_articles(self):
        for i in range(5):
            article_preview = ArticlePreview(size_hint_y=None, height=dp(300))
            self.ids.articles_grid.add_widget(article_preview)
