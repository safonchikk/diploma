from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

from my_screen import MyScreen


def log(login, password):
    MDApp.get_running_app().user = 'user'
    MDApp.get_running_app().creator_flag = True


class LoginScreen(MyScreen):
    def login(self):
        login = self.ids.login_input.text
        password = self.ids.password_input.text
        log(login, password)
