from kivy.lang import Builder
from kivymd.app import MDApp

from creator_edit_profile import CreatorEditProfile
from diploma_page import DiplomaPageScreen
from article_page import ArticlePageScreen
from comment_screen import CommentScreen
from creator_profile_screen import CreatorProfileScreen
from login_screen import LoginScreen
from main_screen import MainScreen
from my_screen_manager import MyScreenManager
from new_video_screen import NewVideoScreen
from registration_screen import RegistrationScreen
from short_page import ShortPageScreen
from update_video_screen import UpdateVideoScreen
from video_page import VideoPageScreen

Builder.load_file('sliding_panel.kv')
Builder.load_file('comment_screen.kv')
Builder.load_file('login_screen.kv')
Builder.load_file('registration_screen.kv')
Builder.load_file('previews/article_preview.kv')
Builder.load_file('previews/creator_article_preview.kv')
Builder.load_file('previews/video_preview.kv')
Builder.load_file('previews/creator_video_preview.kv')
Builder.load_file('previews/creator_preview.kv')
Builder.load_file('previews/short_preview.kv')
Builder.load_file('new_article.kv')
Builder.load_file('new_video.kv')
Builder.load_file('update_video.kv')
Builder.load_file('update_article.kv')
Builder.load_file('creator_profile_screen.kv')
Builder.load_file('video_page.kv')
Builder.load_file('short_page.kv')
Builder.load_file('article_page.kv')
Builder.load_file('diploma_page.kv')
Builder.load_file('creator_edit_profile.kv')


class LifeHealther(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Orange'

        sm = MyScreenManager()

        sm.add_widget(RegistrationScreen(name='registration'))
        sm.add_widget(LoginScreen(name='login'))

        creator_flag = True

        if creator_flag:
            sm.add_widget(CreatorProfileScreen(name='creator_profile'))
            sm.add_widget(VideoPageScreen(name='video_page'))
            sm.add_widget(ShortPageScreen(name='short_page'))
            sm.add_widget(ArticlePageScreen(name='article_page'))
            sm.add_widget(DiplomaPageScreen(name='diploma_page'))
            sm.add_widget(CreatorEditProfile(name='edit_profile'))

            sm.current = 'creator_profile'

        else:
            main_screen = MainScreen(name='main')
            # main_screen.load_articles()
            # main_screen.load_videos()
            # main_screen.load_creators()
            sm.add_widget(main_screen)

            #sm.add_widget(CommentScreen(name='comment'))

        return sm


if __name__ == '__main__':
    LifeHealther().run()
