from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from my_screen import MyScreen
import requests
import hashlib


def log(login, password):
    h = hashlib.sha3_256()
    h.update(bytes(password, 'UTF-8'))
    password = h.hexdigest()
    data = {
        "username": login,
        "password": password
    }
    r = requests.get("https://lifehealther.onrender.com/login", params=data)
    if r.status_code == 404:
        return False
    data = r.json()
    MDApp.get_running_app().user = data['id']
    MDApp.get_running_app().role = data['role']
    return False


class LoginScreen(MyScreen):
    def login(self):
        login = self.ids.login_input.text
        password = self.ids.password_input.text
        if log(login, password):
            MDApp.get_running_app().go_to_page()
        else:
            dialog = MDDialog(
                text="Wrong login or password"
            )
            dialog.open()
