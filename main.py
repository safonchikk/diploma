from kivy.app import App
from kivy.clock import Clock
from kivy.core.clipboard import Clipboard
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, ColorProperty
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window, Animation
from kivy.uix.videoplayer import VideoPlayer


Builder.load_file('sliding_panel.kv')
Builder.load_file('comment_screen.kv')
Builder.load_file('login_screen.kv')
Builder.load_file('registration_screen.kv')


class MainScreen(Screen):

    Window.size = (400, 750)

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


class SlidingPanel(ButtonBehavior, BoxLayout):
    pass


class RegistrationScreen(Screen):
    def register(self):
        role = self.ids.role_spinner.text
        login = self.ids.login_input.text
        password = self.ids.password_input.text
        self.reg(role, login, password)

    def reg(self, role, login, password):
        pass


class LoginScreen(Screen):
    def login(self):
        login = self.ids.login_input.text
        password = self.ids.password_input.text
        self.log(login, password)

    def log(self, login, password):
        pass


class LifeHealther(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(CommentScreen(name='comment'))
        sm.add_widget(RegistrationScreen(name='registration'))
        sm.add_widget(LoginScreen(name='login'))
        return sm


if __name__ == '__main__':
    LifeHealther().run()