from kivy.uix.screenmanager import Screen


class MyScreen(Screen):
    def go_back(self, instance):
        print(self.manager.screen_history)
        if self.manager.screen_history:
            previous_screen = self.manager.screen_history.pop()
            self.manager.current = previous_screen
