from kivy.uix.button import Button
import requests

from author_pages.update_video_screen import UpdateVideoScreen


class CreatorShortPreview(Button):
    def __init__(self, thumbnail, content_id, title='Title', **kwargs):
        super(CreatorShortPreview, self).__init__(**kwargs)
        self.content_id = content_id
        self.ids.thumbnail.texture = thumbnail
        self.ids.title.text = title

    def delete(self):
        requests.delete("https://lifehealther.onrender.com/short/delete/" + str(self.content_id))
        requests.delete("https://lifehealther.onrender.com/content/" + str(self.content_id)+"/delete")

    def create_update(self):
        screen = UpdateVideoScreen(self.content_id, name='update_video')
        self.create_upd(screen)
