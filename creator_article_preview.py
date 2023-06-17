from kivy.uix.button import Button


class CreatorArticlePreview(Button):
    def __init__(self, headline='Headline', text_preview='Text', **kwargs):
        super(CreatorArticlePreview, self).__init__(**kwargs)
        self.ids.headline.text = headline
        self.ids.text_preview.text = text_preview

    def delete(self):
        pass