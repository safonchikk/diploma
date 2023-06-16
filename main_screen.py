from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.button import MDRoundFlatButton

from creator_preview import CreatorPreview
from my_screen import MyScreen
from video_preview import VideoPreview
from article_preview import ArticlePreview
import requests


class MainScreen(MyScreen):

    Window.size = (400, 750)

    def load_articles(self):
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        articles = requests.get("http://127.0.0.1:8000/article/free")
        for i in articles.json().values():
            url = "http://127.0.0.1:8000/article/" + str(i["id"])
            article_info = requests.get(url)
            article_info = article_info.json()
            url = "http://127.0.0.1:8000/user/" + str(i["creator"])
            article_text = article_info["text"]
            if len(article_text) > 115:
                article_text = article_text[:115] + "..."
            creator_info = requests.get(url)
            creator_info = creator_info.json()
            article_preview = ArticlePreview(size_hint_y=None,
                                             height=dp(250),
                                             author_name=creator_info["username"],
                                             headline=article_info["article_name"],
                                             text_preview=article_text)
            layout.add_widget(article_preview)

        scroll_view = ScrollView()
        scroll_view.add_widget(layout)

        self.ids.articles_grid.add_widget(scroll_view)

    def load_videos(self):
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(5):
            video_preview = VideoPreview(size_hint_y=None, height=dp(300))
            layout.add_widget(video_preview)

        scroll_view = ScrollView()
        scroll_view.add_widget(layout)

        self.ids.videos_grid.add_widget(scroll_view)

    def load_creators(self):
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(15):
            creator_preview = CreatorPreview(size_hint_y=None, height=dp(50))
            layout.add_widget(creator_preview)

        scroll_view = ScrollView()
        scroll_view.add_widget(layout)

        self.ids.creators_grid.add_widget(scroll_view)

    def like(self):
        if self.ids.like_icon.source == "images/like.png":
            self.ids.like_icon.source = "images/liked.png"
        else:
            self.ids.like_icon.source = "images/like.png"

    @staticmethod
    def share():
        Clipboard.copy("Linkie")
        popup = Popup(title='Copied', content=Label(text='Link has been copied.'), size_hint=(None, None),
                      size=(200, 100), auto_dismiss=True, overlay_color=(0, 0, 0, 0))
        popup.open()
        Clock.schedule_once(lambda dt: popup.dismiss(), 1)
