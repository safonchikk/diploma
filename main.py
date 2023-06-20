import glob

from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp

from author_pages.creator_edit_profile import CreatorEditProfile
from author_pages.diploma_page import DiplomaPageScreen
from author_pages.article_page import ArticlePageScreen
from author_pages.creator_profile_screen import CreatorProfileScreen
from login_screen import LoginScreen
from main_screen import MainScreen
from my_screen_manager import MyScreenManager
from registration_screen import RegistrationScreen
from author_pages.short_page import ShortPageScreen
from author_pages.sub_page import SubPageScreen
from author_pages.video_page import VideoPageScreen

directories = ['.', 'author_pages', 'previews']

for directory in directories:
    kv_files = glob.glob(f"{directory}/*.kv")

    for kv_file in kv_files:
        Builder.load_file(kv_file)


class LifeHealther(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = None
        self.user = None
        self.role = None

    def go_to_page(self):
        if self.role == "Cr":
            self.sm.add_widget(CreatorProfileScreen(name='creator_profile'))
            self.sm.add_widget(VideoPageScreen(name='video_page'))
            self.sm.add_widget(ShortPageScreen(name='short_page'))
            self.sm.add_widget(ArticlePageScreen(name='article_page'))
            self.sm.add_widget(DiplomaPageScreen(name='diploma_page'))
            self.sm.add_widget(SubPageScreen(name='sub_page'))
            self.sm.add_widget(CreatorEditProfile(name='edit_profile'))

            self.sm.get_screen('creator_profile').load_info()
            self.sm.current = 'creator_profile'

        elif self.role == "Cu":
            main_screen = MainScreen(name='main')

            self.sm.add_widget(main_screen)
            self.sm.current = 'main'
            main_screen.load_articles()
            # main_screen.load_shorts()
            main_screen.load_videos()
            main_screen.load_creators()

            # sm.add_widget(CommentScreen(name='comment'))

    def build(self):
        Window.softinput_mode = 'below_target'

        self.theme_cls.primary_palette = 'Orange'
        self.sm = MyScreenManager()

        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(RegistrationScreen(name='registration'))

        return self.sm


if __name__ == '__main__':
    LifeHealther().run()
