from kivy.metrics import dp

from my_screen import MyScreen
from kivymd.app import MDApp

import requests

from author_pages.new_article_screen import NewArticleScreen
from previews.creator_content_preview import CreatorContentPreview


class SubEditScreen(MyScreen):
    def __init__(self, sub_id, **kwargs):
        super(SubEditScreen, self).__init__(**kwargs)
        self.sub_id = sub_id
        self.ids.content_grid.bind(minimum_height=self.ids.content_grid.setter('height'))
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))

    def load_content(self):
        self.ids.content_grid.clear_widgets()
        creator_id = MDApp.get_running_app().user
        tier_content = requests.get("https://lifehealther.onrender.com/sponsor_tier/creator/content/" + str(self.sub_id))
        if tier_content.json() != {}:
            for i in tier_content.json().values():
                preview = CreatorContentPreview(size_hint_y=None,
                                                height=dp(250),
                                                content_id=i["content_id"],
                                                title=i["content_name"],
                                                content_type=i["content_type"],
                                                sub_id=self.sub_id,
                                                included=True)
                self.ids.content_grid.add_widget(preview)
        content = requests.get("https://lifehealther.onrender.com/sponsor_tier/creator/content/no/" + str(self.sub_id))
        if content.json() != {}:
            for i in content.json().values():
                preview = CreatorContentPreview(size_hint_y=None,
                                                height=dp(250),
                                                content_id=i["content_id"],
                                                title=i["content_name"],
                                                content_type=i["content_type"],
                                                sub_id=self.sub_id,
                                                included=False)
                self.ids.content_grid.add_widget(preview)

