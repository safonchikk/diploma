from kivy.metrics import dp
from kivy.core.image import Image as CoreImage

from my_screen import MyScreen
from kivymd.app import MDApp

import requests
import base64
import os

from previews.video_preview import VideoPreview


class AuthorArticlesScreen(MyScreen):
    def __init__(self, author_id, articles, username, avatar, info, **kwargs):
        super(AuthorArticlesScreen, self).__init__(name='author_articles', **kwargs)
        self.ids.articles_grid.bind(minimum_height=self.ids.articles_grid.setter('height'))
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))
        self.k = 0
        self.author_id = author_id
        self.articles = articles
        self.username = username
        self.avatar = avatar
        self.info = info
        self.load_articles()

    def load_articles(self):
        self.ids.articles_grid.clear_widgets()
        '''if self.articles:
            #for i in self.articles:
                decoded_bytes = base64.b64decode(i["preview"])
                temp_filename = 'temp_image_self_screen_videos_'+str(self.k)+'.png'
                with open(temp_filename, 'wb') as file:
                    file.write(decoded_bytes)
                core_image = CoreImage(temp_filename)
                video_preview = VideoPreview(size_hint_y=None,
                                             height=dp(300),
                                             content_id=i['content_id'],
                                             title=i["title"],
                                             author_name=self.username,
                                             thumbnail=core_image.texture,
                                             creator_id=self.author_id,
                                             author_avatar=self.avatar,
                                             like_count=i["like_count"])
                self.k += 1'''
                #self.ids.articles_grid.add_widget(article_preview)
                #os.remove(temp_filename)
