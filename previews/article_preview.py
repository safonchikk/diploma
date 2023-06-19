from kivy.uix.button import Button

from article_screen import ArticleScreen


class ArticlePreview(Button):
    def __init__(self, author_avatar='images/account.png', author_name='John Doe',
                 headline='Article Headline', content_id=1,
                 text_preview='Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                              'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', **kwargs):
        super(ArticlePreview, self).__init__(**kwargs)
        self.ids.author_avatar.source = author_avatar
        self.ids.author_name.text = author_name
        self.ids.headline.text = headline
        self.ids.text_preview.text = text_preview
        self.content_id = content_id
