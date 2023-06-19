from kivy.uix.button import Button

from article_screen import ArticleScreen


class ArticlePreview(Button):
    def __init__(self,author_name,author_id,headline,text_preview,content_id,like_count, author_avatar, **kwargs):
        super(ArticlePreview, self).__init__(**kwargs)
        if author_avatar == "NO":
            self.ids.author_avatar.source = 'images/account.png'
        else:
            self.ids.author_avatar.texture = author_avatar
        self.ids.author_name.text = author_name
        self.ids.headline.text = headline
        self.ids.text_preview.text = text_preview
        self.content_id = content_id
        self.author_id = author_id,
        self.like_count = like_count
