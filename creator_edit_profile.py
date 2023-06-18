from kivymd.uix.filemanager import MDFileManager

from my_screen import MyScreen


class CreatorEditProfile(MyScreen):
    def __init__(self, **kwargs):
        super(CreatorEditProfile, self).__init__(**kwargs)
        self.chosen_avatar = ''
        self.file_manager = MDFileManager(
            select_path=self.select_path,
            exit_manager=self.exit_manager
        )

    #тут завантаж старі теги і аву
    def load_current_info(self):
        self.ids.save_button.disabled = True
        self.chosen_avatar = ''
        self.ids.avatar_path.text = ''
        #отут
        self.ids.new_avatar.source = 'images/account.png'
        self.ids.info.text = ''

    @staticmethod
    def open_manager(file_manager):
        file_manager.show('\\Games')

    @staticmethod
    def exit_manager(file_manager):
        file_manager.close()

    def select_path(self, path):
        self.chosen_avatar = path
        self.ids.avatar_path.text = path
        self.ids.new_avatar.source = path
        self.ids.save_button.disabled = False
        self.exit_manager(self.file_manager)

    def save_avatar(self):
        pass

    def save_info(self):
        pass
