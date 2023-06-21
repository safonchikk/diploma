import re

from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog

from my_screen import MyScreen
import hashlib
import requests


class AdminScreen(MyScreen):

    def validate_login(self):
        pat = re.compile(r"[A-Za-z0-9_]{5,32}")
        if not re.fullmatch(pat, self.ids.login_input.text):
            self.ids.login_input.error = True
        return not self.ids.login_input.error

    def validate_password(self):
        if len(self.ids.password_input.text) < 8 or len(self.ids.password_input.text) > 32:
            self.ids.password_input.error = True
        return not self.ids.password_input.error

    def validate_second_password(self):
        if self.ids.password_confirm_input.text != self.ids.password_input.text:
            self.ids.password_confirm_input.error = True
        return not self.ids.password_confirm_input.error

    def register(self):
        if not (self.validate_login() & self.validate_password() & self.validate_second_password()):
            return
        role = 'Mo'
        login = self.ids.login_input.text
        password = self.ids.password_input.text
        if self.reg(login, password):
            dialog = MDDialog(
                text='Moderator account created'
            )
        else:
            dialog = MDDialog(
                text='This login is already used'
            )
        dialog.open()

    def reg(self, login, password):
        h = hashlib.sha3_256()
        h.update(bytes(password, 'UTF-8'))
        password = h.hexdigest()
        '''    data = {
            "id":{
                "id": {
                    "username": login,
                    "password": password
                },
                "role": "Cu"
            }
        }
        r = requests.post("https://lifehealther.onrender.com/customer/create", json=data)
        if r.status_code != 201:
            return False
        MDApp.get_running_app().user = r.json()["id"]
        MDApp.get_running_app().role = "Cu"
        data = {
            "creator_id": r.json()["id"]
        }
        r = requests.post("https://lifehealther.onrender.com/customer_mongo/create", json=data)
        '''