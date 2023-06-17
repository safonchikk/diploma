from kivy.metrics import dp
from kivy.uix.screenmanager import Screen

from article_preview import ArticlePreview
from creator_article_preview import CreatorArticlePreview
from my_screen import MyScreen

import requests

from new_article_screen import NewArticleScreen


class ArticlePageScreen(MyScreen):
    def __init__(self, **kwargs):
        super(ArticlePageScreen, self).__init__(**kwargs)
        self.ids.articles_grid.bind(minimum_height=self.ids.articles_grid.setter('height'))
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))
        #self.load_articles()

    def load_articles(self):
        self.ids.articles_grid.clear_widgets()
        articles = requests.get("https://lifehealther.onrender.com/article/creator/19")
        for i in articles.json().values():
            url = "https://lifehealther.onrender.com/article/" + str(i["id"])
            article_info = requests.get(url)
            article_info = article_info.json()
            url = "https://lifehealther.onrender.com/user/" + str(i["creator"])
            article_text = article_info["text"]
            if len(article_text) > 115:
                article_text = article_text[:115] + "..."
            creator_info = requests.get(url)
            creator_info = creator_info.json()
            article_preview = CreatorArticlePreview(size_hint_y=None,
                                                    height=dp(250),
                                                    content_id=i["id"],
                                                    headline=article_info["article_name"],
                                                    text_preview=article_text)

            self.ids.articles_grid.add_widget(article_preview)

    def create_upd(self, upd_screen):
        self.manager.add_widget(upd_screen)
        self.manager.screen_history.append(self.manager.current)
        self.manager.current = 'update_article'

    def create_add(self):
        self.manager.add_widget(NewArticleScreen(name='new_article'))
