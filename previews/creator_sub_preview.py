from kivy.uix.button import Button
import requests

from sub_edit_screen import SubEditScreen
from update_article_screen import UpdateArticleScreen


class CreatorSubPreview(Button):
    def __init__(self, sponsor_tier_id, create_upd, name='Subscription', info='Text', price=0, **kwargs):
        super(CreatorSubPreview, self).__init__(**kwargs)
        self.sponsor_tier_id = sponsor_tier_id
        self.ids.name.text = name
        self.ids.description.text = info
        self.create_upd = create_upd
        self.price = price

    def delete(self):
        requests.delete("https://lifehealther.onrender.com/sponsor_tier/mongo/delete/" + str(self.sponsor_tier_id))
        requests.delete("https://lifehealther.onrender.com/sponsor_tier/" + str(self.sponsor_tier_id) + "/delete")

    def create_update(self):
        screen = SubEditScreen(self.sponsor_tier_id, name='update_sub')
        self.create_upd(screen)
