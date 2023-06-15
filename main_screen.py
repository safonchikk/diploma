from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from creator_preview import CreatorPreview
from video_preview import VideoPreview
from article_preview import ArticlePreview


class MainScreen(Screen):

    #Window.size = (400, 750)

    def load_articles(self):
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(5):
            article_preview = ArticlePreview(size_hint_y=None, height=dp(250))
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

    def share(self):
        Clipboard.copy("Linkie")
        popup = Popup(title='Copied', content=Label(text='Link has been copied.'), size_hint=(None, None),
                      size=(200, 100), auto_dismiss=True, overlay_color=(0, 0, 0, 0))
        popup.open()
        Clock.schedule_once(lambda dt: popup.dismiss(), 1)
