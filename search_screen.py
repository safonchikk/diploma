from textwrap import dedent

from kivy.lang import Builder
from kivymd.app import MDApp

from my_screen import MyScreen


class SearchScreen(MyScreen):
    def __init__(self, query, **kwargs):
        self.videos_grid = Builder.load_string(dedent("""
            MDBoxLayout:
                padding: dp(10)
                size_hint: 1, None
                height: self.minimum_height
                id: videos_grid
            """))

        self.articles_grid = Builder.load_string(dedent("""
                MDBoxLayout:
                    padding: dp(10)
                    size_hint: 1, None
                    height: self.minimum_height
                    id: articles_grid
                """))

        self.creators_grid = Builder.load_string(dedent("""
                MDBoxLayout:
                    padding: dp(10)
                    size_hint: 1, None
                    height: self.minimum_height
                    id: creators_grid
                """))

        super(SearchScreen, self).__init__(name='search', **kwargs)
        self.articles_grid.bind(minimum_height=self.articles_grid.setter('height'))
        self.videos_grid.bind(minimum_height=self.videos_grid.setter('height'))
        self.creators_grid.bind(minimum_height=self.creators_grid.setter('height'))
        self.ids.layout.bind(minimum_height=self.ids.layout.setter('height'))
        self.load_results()
        self.ids.search_input.text = query
        self.query = query

    def load_results(self):
        self.articles_grid.clear_widgets()
        self.videos_grid.clear_widgets()
        self.creators_grid.clear_widgets()
        '''creator_id = MDApp.get_running_app().user
        articles = requests.get("https://lifehealther.onrender.com/article/creator/" + str(creator_id))
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
        self.go_videos()

    def clear_buttons(self):
        self.ids.video_button.md_bg_color = (1, 1, 1, 1)
        self.ids.article_button.md_bg_color = (1, 1, 1, 1)
        self.ids.author_button.md_bg_color = (1, 1, 1, 1)

    def go_videos(self):
        self.ids.grid.clear_widgets()
        self.ids.grid.add_widget(self.videos_grid)
        self.clear_buttons()
        self.ids.video_button.md_bg_color = (.8, .8, .8, 1)

    def go_articles(self):
        self.ids.grid.clear_widgets()
        self.ids.grid.add_widget(self.articles_grid)
        self.clear_buttons()
        self.ids.article_button.md_bg_color = (.8, .8, .8, 1)

    def go_authors(self):
        self.ids.grid.clear_widgets()
        self.ids.grid.add_widget(self.creators_grid)
        self.clear_buttons()
        self.ids.author_button.md_bg_color = (.8, .8, .8, 1)

    def upd_query(self):
        self.query = self.ids.search_input.text
        self.load_results()
