from kivy.uix.button import Button
import requests
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.dialog import MDDialog

from author_pages.update_video_screen import UpdateVideoScreen


class CreatorVideoPreview(Button):
    def __init__(self, thumbnail, content_id, create_upd, title='Title', **kwargs):
        super(CreatorVideoPreview, self).__init__(**kwargs)
        self.content_id = content_id
        self.ids.thumbnail.texture = thumbnail
        self.ids.title.text = title
        self.create_upd = create_upd
        self.dialog = None

    def delete(self):
        title = "Are you sure?"
        if not self.dialog:
            self.dialog = MDDialog(
                title=title,
                buttons=[
                    MDRoundFlatButton(text="Cancel", on_release=self.close_popup),
                    MDRoundFlatButton(text="Yes", on_release=self.confirmed_delete),
                ],
            )
        self.dialog.open()

    def close_popup(self, instance):
        self.dialog.dismiss()

    def confirmed_delete(self):
        requests.delete("https://lifehealther.onrender.com/video/delete/" + str(self.content_id))
        requests.delete("https://lifehealther.onrender.com/content/" + str(self.content_id) + "/delete")

    def create_update(self):
        screen = UpdateVideoScreen(self.content_id, name='update_video')
        self.create_upd(screen)
