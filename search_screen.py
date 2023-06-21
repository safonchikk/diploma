from textwrap import dedent
from kivy.metrics import dp

from previews.article_preview import ArticlePreview
from previews.creator_preview import CreatorPreview
from previews.video_preview import VideoPreview
from kivy.core.image import Image as CoreImage
import base64
import os
import requests
from kivy.lang import Builder
from kivymd.app import MDApp

from my_screen import MyScreen


class SearchScreen(MyScreen):
    def __init__(self, query, **kwargs):
        self.k = 0
        self.articles = []
        self.videos = []
        self.authors = []
        self.videos_grid = Builder.load_string(dedent("""
            MDBoxLayout:
                padding: dp(10)
                size_hint: 1, None
                height: self.minimum_height
                id: videos_grid
            """))

        self.articles_grid = Builder.load_string(dedent("""
                MDBoxLayout:
                    padding: dp(10)
                    size_hint: 1, None
                    height: self.minimum_height
                    id: articles_grid
                """))

        self.creators_grid = Builder.load_string(dedent("""
                MDBoxLayout:
                    padding: dp(10)
                    size_hint: 1, None
                    height: self.minimum_height
                    id: creators_grid
                """))

        super(SearchScreen, self).__init__(name='search', **kwargs)
        self.articles_grid.bind(minimum_height=self.articles_grid.setter('height'))
        self.videos_grid.bind(minimum_height=self.videos_grid.setter('height'))
        self.creators_grid.bind(minimum_height=self.creators_grid.setter('height'))
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))
        self.load_results()
        self.ids.search_input.text = query
        self.query = query

    def load_results(self):
        customer_id = MDApp.get_running_app().user
        self.articles_grid.clear_widgets()
        self.videos_grid.clear_widgets()
        self.creators_grid.clear_widgets()
        result = requests.get("https://lifehealther.onrender.com/fined/" + str(customer_id) + "/" + str(self.query)).json()
        self.authors = result["authors"]
        self.videos = result["videos"]
        self.articles = result["articles"]
        if self.videos:
            for i in self.videos:
                decoded_bytes = base64.b64decode(i["preview"])
                temp_filename = 'temp_image_self_search_' + str(self.k) + str(i['content_id']) + '.png'
                with open(temp_filename, 'wb') as file:
                    file.write(decoded_bytes)
                core_image = CoreImage(temp_filename)
                avatar = i["avatar"]
                os.remove(temp_filename)
                if avatar != "NO":
                    decoded_bytes = base64.b64decode(avatar)
                    temp_filename = 'temp_search_scren_avatar_nnnn_' + str(self.k) + str(i['content_id']) +'.png'
                    with open(temp_filename, 'wb') as file:
                        file.write(decoded_bytes)
                    core_image = CoreImage(temp_filename)
                    avatar = core_image.texture
                    os.remove(temp_filename)


                video_preview = VideoPreview(size_hint_y=None,
                                             height=dp(300),
                                             content_id=i['content_id'],
                                             title=i["video_name"],
                                             author_name=i["username"],
                                             thumbnail=core_image.texture,
                                             creator_id=i["creator_id"],
                                             author_avatar=avatar,
                                             like_count=i["like_count"])
                self.k += 1
                self.videos_grid.add_widget(video_preview)

        if self.articles:
            for i in self.articles:
                text_preview = i["text"]
                if len(text_preview) > 115:
                    text_preview = text_preview[:115] + "..."
                avatar = i["avatar"]
                if avatar != "NO":
                    decoded_bytes = base64.b64decode(avatar)
                    temp_filename = 'temp_search_scren_avatar_nnnn_' + str(self.k) + str(i['content_id']) + '.png'
                    with open(temp_filename, 'wb') as file:
                        file.write(decoded_bytes)
                    core_image = CoreImage(temp_filename)
                    avatar = core_image.texture
                    os.remove(temp_filename)
                article_preview = ArticlePreview(size_hint_y=None,
                                                 height=dp(300),
                                                 content_id=i['content_id'],
                                                 author_id=i["creator_id"],
                                                 author_name=i["username"],
                                                 headline=i["article_name"],
                                                 text_preview=text_preview,
                                                 author_avatar=avatar,
                                                 like_count=i["like_count"])
                self.articles_grid.add_widget(article_preview)
        if self.authors:
            for i in self.authors:
                avatar = i["avatar"]
                if avatar != "NO":
                    decoded_bytes = base64.b64decode(avatar)
                    temp_filename = 'temp_avatar_search_self_0' + str(self.k) + '.png'
                    with open(temp_filename, 'wb') as file:
                        file.write(decoded_bytes)
                    core_image = CoreImage(temp_filename)
                    os.remove(temp_filename)
                else:
                    core_image = CoreImage("images/account.png")
                creator_preview = CreatorPreview(size_hint_y=None, height=dp(50), author_id=i['id'],
                                                 name=i["username"], avatar=core_image.texture)
                self.creators_grid.add_widget(creator_preview)
                self.k += 1

        self.go_videos()

    def clear_buttons(self):
        self.ids.video_button.md_bg_color = (1, 1, 1, 1)
        self.ids.article_button.md_bg_color = (1, 1, 1, 1)
        self.ids.author_button.md_bg_color = (1, 1, 1, 1)

    def go_videos(self):
        self.ids.grid.clear_widgets()
        self.ids.grid.add_widget(self.videos_grid)
        self.clear_buttons()
        self.ids.video_button.md_bg_color = (.8, .8, .8, 1)

    def go_articles(self):
        self.ids.grid.clear_widgets()
        self.ids.grid.add_widget(self.articles_grid)
        self.clear_buttons()
        self.ids.article_button.md_bg_color = (.8, .8, .8, 1)

    def go_authors(self):
        self.ids.grid.clear_widgets()
        self.ids.grid.add_widget(self.creators_grid)
        self.clear_buttons()
        self.ids.author_button.md_bg_color = (.8, .8, .8, 1)

    def upd_query(self):
        self.query = self.ids.search_input.text
        self.load_results()
