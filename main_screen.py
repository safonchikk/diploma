import os

from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.videoplayer import VideoPlayer
from kivymd.app import MDApp

from kivy.core.image import Image as CoreImage

from article_screen import ArticleScreen
from creator_screen import CreatorScreen
from previews.creator_preview import CreatorPreview
from my_screen import MyScreen
from previews.video_preview import VideoPreview
from previews.article_preview import ArticlePreview
import requests
import base64
import logging
import tempfile

from short import Short
from video_screen import VideoScreen
from shorts_player import ShortsPlayer


class MainScreen(MyScreen):

    #Window.size = (400, 750)
    k = 0

    def load_articles(self):
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        articles = requests.get("https://lifehealther.onrender.com/article/free")
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
            article_preview = ArticlePreview(size_hint_y=None,
                                             height=dp(250),
                                             author_name=creator_info["username"],
                                             headline=article_info["article_name"],
                                             text_preview=article_text,
                                             content_id=i['id'],
                                             on_release=lambda instance: self.open_article(article_preview.content_id))
            layout.add_widget(article_preview)

        scroll_view = ScrollView()
        scroll_view.add_widget(layout)

        self.ids.articles_grid.add_widget(scroll_view)

    def open_article(self, content_id):
        article_screen = ArticleScreen(content_id)
        self.manager.add_widget(article_screen)
        self.manager.screen_history.append(self.manager.current)
        self.manager.current = 'article'

    def load_shorts(self):
        layout = GridLayout(cols=1, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        for i in range(3):
            short = Short(content_id=1, size_hint=(1, None), height=Window.height-dp(120))
            layout.add_widget(short)

        scroll_view = ScrollView()
        scroll_view.add_widget(layout)

        self.ids.shorts_player.add_widget(scroll_view)

    def load_videos(self):
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        # response = requests.get("https://lifehealther.onrender.com/video/30", stream=True)
        # temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
        # file_path = temp_file.name
        #
        # with open(file_path, 'wb') as f:
        #     for chunk in response.iter_content(chunk_size=1024):
        #         f.write(chunk)
        #
        # # Вставка відео у VideoPlayer
        # self.ids.video.source = file_path
        videos = requests.get("https://lifehealther.onrender.com/video/free")
        k = 0
        for i in videos.json().values():
            url = "https://lifehealther.onrender.com/video/info/" + str(i["id"])
            video_info = requests.get(url)
            video_info = video_info.json()
            decoded_bytes = base64.b64decode(video_info["preview"])
            temp_filename = 'temp_image' + str(k) +"_" + str(i["id"]) + '.png'
            with open(temp_filename, 'wb') as file:
                file.write(decoded_bytes)

            # Створення об'єкта CoreImage з тимчасового зображення
            core_image = CoreImage(temp_filename)
            url = "https://lifehealther.onrender.com/user/" + str(i["creator"])
            creator_info = requests.get(url)
            creator_info = creator_info.json()
            video_preview = VideoPreview(size_hint_y=None,
                                         height=dp(300),
                                         author_name=creator_info["username"],
                                         thumbnail=core_image.texture,
                                         title=video_info["video_name"],
                                         content_id=i['id'],
                                         on_release=lambda instance: self.open_video(video_preview.content_id))
            layout.add_widget(video_preview)
            os.remove(temp_filename)
        scroll_view = ScrollView()
        scroll_view.add_widget(layout)

        self.ids.videos_grid.add_widget(scroll_view)

    def open_video(self, content_id):
        video_screen = VideoScreen(content_id)
        self.manager.add_widget(video_screen)
        self.manager.screen_history.append(self.manager.current)
        self.manager.current = 'video'

    def load_creators(self):
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        customer_id = MDApp.get_running_app().user
        creators = requests.get("https://lifehealther.onrender.com/customer/subs/" + str(customer_id)).json()
        for i in creators["creators"]:
            avatar = i["avatar"]
            if avatar != "NO":
                decoded_bytes = base64.b64decode(avatar)
                temp_filename = 'temp_avatar' + str(MainScreen.k) + '.png'
                with open(temp_filename, 'wb') as file:
                    file.write(decoded_bytes)
                core_image = CoreImage(temp_filename)
                os.remove(temp_filename)
            else:
                core_image = CoreImage("images/account.png")
            creator_preview = CreatorPreview(size_hint_y=None, height=dp(50), author_id=i['id'],
                                             name=i["username"], avatar=core_image.texture,
                                             on_release=lambda instance: self.open_creator(creator_preview.author_id))
            layout.add_widget(creator_preview)
            MainScreen.k += 1

        scroll_view = ScrollView()
        scroll_view.add_widget(layout)

        self.ids.creators_grid.add_widget(scroll_view)

    def open_creator(self, author_id):
        creator_screen = CreatorScreen(author_id)
        self.manager.add_widget(creator_screen)
        self.manager.screen_history.append(self.manager.current)
        self.manager.current = 'creator'

    def like(self):
        if self.ids.like_icon.source == "images/like.png":
            self.ids.like_icon.source = "images/liked.png"
        else:
            self.ids.like_icon.source = "images/like.png"
