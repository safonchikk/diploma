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

from previews.creator_preview import CreatorPreview
from my_screen import MyScreen
from previews.video_preview import VideoPreview
from previews.article_preview import ArticlePreview
import requests
import base64
import logging
import tempfile

from search_screen import SearchScreen
from short import Short
from video_screen import VideoScreen
from shorts_player import ShortsPlayer


class MainScreen(MyScreen):

    #Window.size = (400, 750)
    k = 0

    def load_articles(self):
        customer_id = MDApp.get_running_app().user
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        r = requests.get("https://lifehealther.onrender.com/recomendetion/article/" + str(customer_id)).json()
        articles = r["contents"]
        if articles:
            for i in articles:
                avatar = i["avatar"]
                if avatar != "NO":
                    decoded_bytes = base64.b64decode(i["avatar"])
                    temp_filename = 'temp_article_avatar' + str(MainScreen.k) + "_" + str(i["content_id"]) + '.png'
                    with open(temp_filename, 'wb') as file:
                        file.write(decoded_bytes)
                    core_image = CoreImage(temp_filename)
                    avatar = core_image.texture
                text = i["text"]
                if len(text) > 115:
                    text = text[:115]
                article_preview = ArticlePreview(size_hint_y=None,
                                                 height=dp(250),
                                                 author_name=i["username"],
                                                 author_id=i["creator_id"],
                                                 headline=i["article_name"],
                                                 text_preview=text,
                                                 content_id=i['content_id'],
                                                 like_count=i["like_count"],
                                                 author_avatar=avatar)
                if avatar != "NO":
                    MainScreen.k += 1
                    os.remove(temp_filename)
                layout.add_widget(article_preview)

        scroll_view = ScrollView()
        scroll_view.add_widget(layout)

        self.ids.articles_grid.add_widget(scroll_view)

    def load_shorts(self):
        layout = GridLayout(cols=1, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        customer_id = MDApp.get_running_app().user
        r = requests.get("https://lifehealther.onrender.com/recomendetion/short/" + str(customer_id)).json()
        shorts = r["contents"]
        if shorts:
            for i in shorts:
                avatar = i["avatar"]
                if avatar != "NO":
                    decoded_bytes = base64.b64decode(i["avatar"])
                    temp_filename = 'temp_article_avatar' + str(MainScreen.k) + "_" + str(i["content_id"]) + '.png'
                    with open(temp_filename, 'wb') as file:
                        file.write(decoded_bytes)
                    core_image = CoreImage(temp_filename)
                    avatar = core_image.texture
                short = Short(size_hint=(1, None), height=Window.height-dp(120),
                              content_id=i["content_id"],
                              title=i["video_name"],
                              creator_id=i["creator_id"],
                              avatar=avatar,
                              like_count=i["like_count"])
                layout.add_widget(short)
                os.remove(temp_filename)

        scroll_view = ScrollView()
        scroll_view.add_widget(layout)

        self.ids.shorts_player.add_widget(scroll_view)

    def load_videos(self):
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        customer_id = MDApp.get_running_app().user
        r = requests.get("https://lifehealther.onrender.com/recomendetion/video/" + str(customer_id)).json()
        videos = r["contents"]
        if videos:
            for i in videos:
                avatar = i["avatar"]
                if avatar != "NO":
                    decoded_bytes = base64.b64decode(i["avatar"])
                    temp_filename = 'temp_video_avatar' + str(MainScreen.k) + "_" + str(i["content_id"]) + '.png'
                    with open(temp_filename, 'wb') as file:
                        file.write(decoded_bytes)
                    core_image = CoreImage(temp_filename)
                    avatar = core_image.texture
                    MainScreen.k += 1
                    os.remove(temp_filename)
                decoded_bytes = base64.b64decode(i["preview"])
                temp_filename = 'temp_image' + str(MainScreen.k) +"_" + str(i["content_id"]) + '.png'
                with open(temp_filename, 'wb') as file:
                    file.write(decoded_bytes)
                core_image = CoreImage(temp_filename)
                video_preview = VideoPreview(size_hint_y=None,
                                             height=dp(300),
                                             content_id=i['content_id'],
                                             title=i["video_name"],
                                             author_name=i["username"],
                                             thumbnail=core_image.texture,
                                             creator_id=i["creator_id"],
                                             author_avatar=avatar,
                                             like_count=i["like_count"])
                layout.add_widget(video_preview)
                os.remove(temp_filename)
                MainScreen.k += 1
        scroll_view = ScrollView()
        scroll_view.add_widget(layout)

        self.ids.videos_grid.add_widget(scroll_view)

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
                                             name=i["username"], avatar=core_image.texture)
            layout.add_widget(creator_preview)
            MainScreen.k += 1

        scroll_view = ScrollView()
        scroll_view.add_widget(layout)

        self.ids.creators_grid.add_widget(scroll_view)

    def search(self):
        if self.ids.search_input.text != '':
            self.manager.add_widget(SearchScreen(self.ids.search_input.text))
            self.manager.screen_history.append(self.manager.current)
            self.manager.current = 'search'
