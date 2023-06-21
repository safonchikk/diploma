from kivy.metrics import dp
from kivy.core.image import Image as CoreImage

from my_screen import MyScreen
from kivymd.app import MDApp

import requests
import base64
import os

from previews.article_preview import ArticlePreview


class AuthorArticlesScreen(MyScreen):
    def __init__(self, author_id, articles, username, avatar, info, **kwargs):
        super(AuthorArticlesScreen, self).__init__(name='author_articles', **kwargs)
        self.ids.articles_grid.bind(minimum_height=self.ids.articles_grid.setter('height'))
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))
        self.author_id = author_id
        self.articles = articles
        self.username = username
        self.avatar = avatar
        self.info = info
        self.load_articles()

    def load_articles(self):
        self.ids.articles_grid.clear_widgets()
        if self.articles:
            for i in self.articles:
                text_preview = i["text"]
                article_preview = ArticlePreview(size_hint_y=None,
                                                 height=dp(300),
                                                 content_id=i['content_id'],
                                                 author_id=self.author_id,
                                                 author_name=self.username,
                                                 headline=i["headline"],
                                                 text_preview=i["text"],
                                                 author_avatar=self.avatar,
                                                 like_count=i["like_count"])
                self.ids.articles_grid.add_widget(article_preview)
