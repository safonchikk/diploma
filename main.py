from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from comment_screen import CommentScreen
from creator_profile_screen import CreatorProfileScreen
from login_screen import LoginScreen
from main_screen import MainScreen
from new_video_screen import NewVideoScreen
from registration_screen import RegistrationScreen
from sliding_panel import SlidingPanel

Builder.load_file('sliding_panel.kv')
Builder.load_file('comment_screen.kv')
Builder.load_file('login_screen.kv')
Builder.load_file('registration_screen.kv')
Builder.load_file('article_preview.kv')
Builder.load_file('video_preview.kv')
Builder.load_file('creator_preview.kv')
Builder.load_file('new_article.kv')
Builder.load_file('new_video.kv')
Builder.load_file('creator_profile_screen.kv')


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
        return CreatorProfileScreen()


if __name__ == '__main__':
    LifeHealther().run()
