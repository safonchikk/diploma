from kivy.uix.button import Button


class VideoPreview(Button):
    def __init__(self, author_avatar='images/account.png',
                 author_name='John Doe',
                 thumbnail='images/thumbnail.jpg',
                 title='Lorem ipsum dolor sit amet.', **kwargs):
        super(VideoPreview, self).__init__(**kwargs)
        self.ids.author_avatar.source = author_avatar
        self.ids.author_name.text = author_name
        self.ids.thumbnail.source = thumbnail
        self.ids.title.text = title
