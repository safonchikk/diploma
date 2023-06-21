from kivymd.app import MDApp

from my_screen import MyScreen


class SearchScreen(MyScreen):
    def __init__(self, **kwargs):
        super(SearchScreen, self).__init__(**kwargs)
        self.ids.articles_grid.bind(minimum_height=self.ids.articles_grid.setter('height'))
        self.ids.videos_grid.bind(minimum_height=self.ids.videos_grid.setter('height'))
        self.ids.creators_grid.bind(minimum_height=self.ids.creators_grid.setter('height'))
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))

    def load_results(self):
        self.ids.articles_grid.clear_widgets()
        self.ids.videos_grid.clear_widgets()
        self.ids.creators_grid.clear_widgets()
        creator_id = MDApp.get_running_app().user
        '''articles = requests.get("https://lifehealther.onrender.com/article/creator/" + str(creator_id))
        if articles.json() != {}:
            for i in articles.json().values():
                url = "https://lifehealther.onrender.com/article/" + str(i["id"])
                article_info = requests.get(url)
                article_info = article_info.json()
                article_text = article_info["text"]
                if len(article_text) > 115:
                    article_text = article_text[:115] + "..."
                article_preview = CreatorArticlePreview(size_hint_y=None,
                                                        height=dp(250),
                                                        content_id=i["id"],
                                                        headline=article_info["article_name"],
                                                        text_preview=article_text,
                                                        create_upd=self.create_upd
                                                        )
                self.ids.articles_grid.add_widget(article_preview)'''