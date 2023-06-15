from kivy.uix.screenmanager import Screen


class LoginScreen(Screen):
    def login(self):
        login = self.ids.login_input.text
        password = self.ids.password_input.text
        self.log(login, password)

    def log(self, login, password):
        pass
