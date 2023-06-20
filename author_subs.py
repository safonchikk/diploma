from kivy.metrics import dp
from kivy.core.image import Image as CoreImage

from my_screen import MyScreen
from kivymd.app import MDApp

import requests
import base64
import os

from previews.sub_preview import SubPreview


class AuthorSubsScreen(MyScreen):
    def __init__(self, author_id, sponsor_tiers, **kwargs):
        super(AuthorSubsScreen, self).__init__(name='author_subs', **kwargs)
        self.ids.subs_grid.bind(minimum_height=self.ids.subs_grid.setter('height'))
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))
        self.sponsor_tiers = sponsor_tiers
        self.author_id = author_id
        self.load_subs()

    def load_subs(self):
        self.ids.subs_grid.clear_widgets()
        sponsor_tiers = self.sponsor_tiers
        if  sponsor_tiers:
            for i in sponsor_tiers:
                video_preview = SubPreview(size_hint_y=None,
                                           height=dp(300),
                                           sponsor_tier_id=i["sponsor_tier_id"],
                                           name=i["name"],
                                           info=i["info"],
                                           price=i["price"],
                                           subbed=i["subbed"])
                self.ids.subs_grid.add_widget(video_preview)
