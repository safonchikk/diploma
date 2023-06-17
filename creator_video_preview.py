from kivy.uix.button import Button
from kivy.properties import ObjectProperty
import requests


class CreatorVideoPreview(Button):
    def __init__(self, thumbnail, content_id, title='Title', **kwargs):
        super(CreatorVideoPreview, self).__init__(**kwargs)
        self.content_id = content_id
        self.ids.thumbnail.texture = thumbnail
        self.ids.title.text = title

    def delete(self):
        requests.delete("https://lifehealther.onrender.com/video/delete/" + str(self.content_id))
        requests.delete("https://lifehealther.onrender.com/content/" + str(self.content_id)+"/delete")