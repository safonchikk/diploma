from kivy.uix.button import Button
import requests

from update_article_screen import UpdateArticleScreen


class CreatorContentPreview(Button):
    def __init__(self, content_id, **kwargs):
        super(CreatorContentPreview, self).__init__(**kwargs)
        #self.ids.title.text =
        #self.ids.type.text =
        self.included = False
        #...
        if self.included:
            self.ids.add_button.opacity = 0
            self.ids.add_button.disabled = True
        else:
            self.ids.delete_button.opacity = 0
            self.ids.delete_button.disabled = True

    def delete(self):
        ...

    def add(self):
        ...
