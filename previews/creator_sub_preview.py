from kivy.uix.button import Button
import requests

from update_article_screen import UpdateArticleScreen


class CreatorSubPreview(Button):
    def __init__(self, sponsor_tier_id, create_upd, headline='Headline', info='Text', price=0, **kwargs):
        super(CreatorSubPreview, self).__init__(**kwargs)
        self.sponsor_tier_id = sponsor_tier_id
        self.ids.headline.text = headline
        self.ids.info.text = info
        self.create_upd = create_upd
        self.price = price

    def delete(self):
        requests.delete("https://lifehealther.onrender.com/sponsor_tier/mongo/delete/" + str(self.sponsor_tier_id))
        requests.delete("https://lifehealther.onrender.com/sponsor_tier/" + str(self.sponsor_tier_id) + "/delete")

    def create_update(self):
        screen = UpdateArticleScreen(self.sponsor_tier_id, name='update_article')
        self.create_upd(screen)
