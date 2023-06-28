from textwrap import dedent

from plyer import filechooser

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.button import Button

from kivy.utils import platform


if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([
        Permission.WRITE_EXTERNAL_STORAGE,
        Permission.READ_EXTERNAL_STORAGE,
        Permission.INTERNET,
    ])


class FileChoose(Button):

    selection = ListProperty([])

    def choose(self):
        filechooser.open_file(on_selection=self.handle_selection)

    def handle_selection(self, selection):
        self.selection = selection

    def on_selection(self, *a, **k):
        App.get_running_app().root.ids.result.text = str(self.selection)


class ChooserApp(App):

    def build(self):
        return Builder.load_string(dedent('''
            <FileChoose>:
            BoxLayout:
                BoxLayout:
                    orientation: 'vertical'
                    TextInput:
                        id: result
                        text: ''
                        hint_text: 'selected path'
                    FileChoose:
                        size_hint_y: 0.1
                        on_release: self.choose()
                        text: 'Select a file'
        '''))


