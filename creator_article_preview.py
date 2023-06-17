from kivy.uix.button import Button
import requests


class CreatorArticlePreview(Button):
    def __init__(self, content_id, headline='Headline', text_preview='Text', **kwargs):
        super(CreatorArticlePreview, self).__init__(**kwargs)
        self.content_id = content_id
        self.ids.headline.text = headline
        self.ids.text_preview.text = text_preview

    def delete(self):
        requests.delete("https://lifehealther.onrender.com/article/delete/" + str(self.content_id))
        requests.delete("https://lifehealther.onrender.com/content/" + str(self.content_id) + "/delete")