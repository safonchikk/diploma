from kivy.uix.image import Image
from kivymd.uix.filemanager import MDFileManager

from my_screen import MyScreen


class DiplomaPageScreen(MyScreen):
    def __init__(self, **kwargs):
        super(DiplomaPageScreen, self).__init__(**kwargs)
        self.ids.diplomas_grid.bind(minimum_height=self.ids.diplomas_grid.setter('height'))
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))
        self.chosen_diploma = ''
        self.file_manager = MDFileManager(
            select_path=self.select_path,
            exit_manager=self.exit_manager
        )

    def load_diplomas(self):
        self.ids.diplomas_grid.clear_widgets()
        for i in range(5):
            diploma = Image(source='images/qq.jpg')
            self.ids.diplomas_grid.add_widget(diploma)

    @staticmethod
    def open_manager(file_manager):
        file_manager.show('\\Games')

    def exit_manager(self, file_manager):
        file_manager.close()
        self.load_diplomas()

    def select_path(self, path):
        self.chosen_diploma = path
        self.exit_manager(self.file_manager)
