from kivy.uix.button import Button
import requests

from author_pages.update_article_screen import UpdateArticleScreen


class CreatorArticlePreview(Button):
    def __init__(self, content_id, create_upd, headline='Headline', text_preview='Text', **kwargs):
        super(CreatorArticlePreview, self).__init__(**kwargs)
        self.content_id = content_id
        self.ids.headline.text = headline
        self.ids.text_preview.text = text_preview
        self.create_upd = create_upd

    def delete(self):
        requests.delete("https://lifehealther.onrender.com/article/delete/" + str(self.content_id))
        requests.delete("https://lifehealther.onrender.com/content/" + str(self.content_id) + "/delete")

    def create_update(self):
        screen = UpdateArticleScreen(self.content_id, name='update_article')
        self.create_upd(screen)
