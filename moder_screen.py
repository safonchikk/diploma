import os

import requests

from my_screen import MyScreen
import base64
from kivy.core.image import Image as CoreImage


class ModerScreen(MyScreen):
    def __init__(self, **kwargs):
        super(ModerScreen, self).__init__(name='moder', **kwargs)
        r = requests.get("https://lifehealther.onrender.com/moder/diplomas").json()
        self.diplomas = r["diplomas"]
        self.iter = 0
        if self.iter < len(self.diplomas):
            self.load_next()

    def load_next(self):
        decoded_bytes = base64.b64decode(self.diplomas[self.iter]["file"])
        temp_filename = 'temp_diploma_moder' + str(self.diplomas[self.iter]["id"]) + '.png'
        with open(temp_filename, 'wb') as file:
            file.write(decoded_bytes)
        core_image = CoreImage(temp_filename)
        os.remove(temp_filename)
        self.ids.diploma.texture = core_image.texture

    def accept(self):
        r = requests.put("https://lifehealther.onrender.com/diploma/update/" + str(self.diplomas[self.iter]["id"]))
        self.iter += 1
        if self.iter < len(self.diplomas):
            self.load_next()

    def reject(self):
        r = requests.delete("https://lifehealther.onrender.com/diploma/delete/" + str(self.diplomas[self.iter]["id"]))
        self.iter += 1
        if self.iter < len(self.diplomas):
            self.load_next()
