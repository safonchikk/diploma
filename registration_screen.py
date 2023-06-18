import re

from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog

from my_screen import MyScreen


class RegistrationScreen(MyScreen):

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
            dialog = MDDialog(
                text='Some data is invalid'
            )
            return
        role = ''
        if self.ids.creator_checkbox.active:
            role = 'Cr'
        else:
            role = 'Cu'
        login = self.ids.login_input.text
        password = self.ids.password_input.text
        if self.reg(role, login, password):
            MDApp.get_running_app().go_to_page()
        else:
            dialog = MDDialog(
                text='This login is already used'
            )
            dialog.open()


    def reg(self, role, login, password):
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
        return True