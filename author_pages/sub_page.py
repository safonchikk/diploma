from kivy.metrics import dp

from author_pages.new_sub_screen import NewSubScreen
from previews.creator_sub_preview import CreatorSubPreview
from my_screen import MyScreen
from kivymd.app import MDApp

import requests

from author_pages.new_article_screen import NewArticleScreen


class SubPageScreen(MyScreen):
    def __init__(self, **kwargs):
        super(SubPageScreen, self).__init__(**kwargs)
        self.ids.subs_grid.bind(minimum_height=self.ids.subs_grid.setter('height'))
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))

    def load_subs(self):
        self.ids.subs_grid.clear_widgets()
        creator_id = MDApp.get_running_app().user
        sponsor_tiers = requests.get("https://lifehealther.onrender.com/sponsor_tier/creator/" + str(creator_id))
        if sponsor_tiers.json() != {}:
            for i in sponsor_tiers.json().values():
                url = "https://lifehealther.onrender.com/sponsor_tier/mongo/" + str(i["id"])
                sponsor_tiers_info = requests.get(url)
                sponsor_tiers_info = sponsor_tiers_info.json()
                info = sponsor_tiers_info["info"]
                sponsor_tier_preview = CreatorSubPreview(size_hint_y=None,
                                                        height=dp(250),
                                                        sponsor_tier_id=i["id"],
                                                        name=i["name"],
                                                        info=info,
                                                        price=i["price"],
                                                        create_upd=self.create_upd
                                                        )
                self.ids.subs_grid.add_widget(sponsor_tier_preview)

    def create_upd(self, upd_screen):
        self.manager.add_widget(upd_screen)
        self.manager.screen_history.append(self.manager.current)
        self.manager.current = 'update_sub'

    def create_add(self):
        self.manager.add_widget(NewSubScreen(name='new_sub'))
