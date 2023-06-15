import requests
from kivy.app import App
from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivymd.uix.filemanager import MDFileManager
import hashlib
import re

from kivymd.app import MDApp

Builder.load_file('sliding_panel.kv')
Builder.load_file('comment_screen.kv')
Builder.load_file('login_screen.kv')
Builder.load_file('registration_screen.kv')
Builder.load_file('article_preview.kv')
Builder.load_file('video_preview.kv')
Builder.load_file('creator_preview.kv')
Builder.load_file('new_article.kv')
Builder.load_file('new_video.kv')


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


class CommentScreen(Screen):
    pass


class ArticlePreview(Button):
    def __init__(self, author_avatar='images/account.png', author_name='John Doe',
                 headline='Article Headline',
                 text_preview='Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                              'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', **kwargs):
        super(ArticlePreview, self).__init__(**kwargs)
        self.ids.author_avatar.source = author_avatar
        self.ids.author_name.text = author_name
        self.ids.headline.text = headline
        self.ids.text_preview.text = text_preview


class VideoPreview(Button):
    pass


class CreatorPreview(Button):
    pass


class SlidingPanel(ButtonBehavior, BoxLayout):
    pass


class RegistrationScreen(Screen):
    def validate_login(self):
        pat = re.compile(r"[A-Za-z0-9_]{5,32}")
        if not re.fullmatch(pat, self.ids.login_input.text):
            self.ids.login_input.error = True

    def validate_password(self):
        if len(self.ids.password_input.text) < 8 or len(self.ids.password_input.text) > 32:
            self.ids.password_input.error = True

    def validate_second_password(self):
        if self.ids.password_confirm_input.text != self.ids.password_input.text:
            self.ids.password_confirm_input.error = True

    def register(self):
        role = ''
        if self.ids.creator_checkbox.active:
            role = 'Cr'
        else:
            role = 'Cu'
        #print(role)
        login = self.ids.login_input.text
        password = self.ids.password_input.text
        self.reg(role, login, password)

    def reg(self, role, login, password):
        return 0
        '''h = hashlib.sha3_256()
        h.update(bytes(password, 'UTF-8'))
        password = h.hexdigest()
        if role == "Viewer":
            data = {
                "id":{
                    "id": {
                        "username": login,
                        "password": password
                    },
                    "role": "Cu"
                }
            }
            r = requests.post("https://lifehealther.onrender.com/customer/create", json=data)
        else:
            data = {
                "id": {
                    "id": {
                        "username": login,
                        "password": password
                    },
                    "role": "Cr"
                }
            }
            r = requests.post("https://lifehealther.onrender.com/creator/create", json=data)'''


class LoginScreen(Screen):
    def login(self):
        login = self.ids.login_input.text
        password = self.ids.password_input.text
        self.log(login, password)

    def log(self, login, password):
        pass


class NewArticleScreen(Screen):
    def publish(self):
        headline = self.ids.headline.text
        article_text = self.ids.article_text.text
        tags = self.ids.tags.text
        data = {
            "creator": 19,
            'content_type': "article",
            'like_count': 0,
            'is_paid': False
        }
        r = requests.post("http://127.0.0.1:8000/content/create", json=data)
        data = {
            "content_id": r.json()["id"],
            "article_name": headline,
            "text": article_text,
            "keywords": tags

        }
        r = requests.post("http://127.0.0.1:8000/article/create", json=data)


class NewVideoScreen(Screen):
    def __init__(self, **kwargs):
        super(NewVideoScreen, self).__init__(**kwargs)
        self.chosen_video = ''
        self.chosen_thumbnail = ''
        self.video_file_manager = MDFileManager(
            select_path=self.select_video_path,
            exit_manager=self.exit_manager
        )
        self.thumbnail_file_manager = MDFileManager(
            select_path=self.select_thumbnail_path,
            exit_manager=self.exit_manager
        )

    def open_manager(self, file_manager):
        file_manager.show('\\Games')

    def exit_manager(self, file_manager):
        file_manager.close()

    def select_video_path(self, path):
        print(path)
        self.chosen_video = path
        self.exit_manager(self.video_file_manager)

    def select_thumbnail_path(self, path):
        print(path)
        self.chosen_thumbnail = path
        self.exit_manager(self.thumbnail_file_manager)

    def publish(self):
        title = self.ids.title.text
        tags = self.ids.tags.text
        video_path = self.chosen_video
        thumbnail_path = self.chosen_thumbnail


class LifeHealther(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Orange'

        main_screen = MainScreen(name='main')
        main_screen.load_articles()
        main_screen.load_videos()
        main_screen.load_creators()
        sm = ScreenManager()
        sm.add_widget(main_screen)
        sm.add_widget(CommentScreen(name='comment'))
        sm.add_widget(RegistrationScreen(name='registration'))
        sm.add_widget(LoginScreen(name='login'))
        #return sm
        return NewVideoScreen()


if __name__ == '__main__':
    LifeHealther().run()