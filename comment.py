from kivy.uix.button import Button
from kivy.uix.widget import Widget


class Comment(Widget):
    def __init__(self, author_login, text, liked, comment_id, **kwargs):
        super(Comment, self).__init__(**kwargs)
        self.ids.author_login.text = author_login
        self.ids.text.text = text
        self.liked = liked
        self.comment_id = comment_id

        if self.liked:
            self.ids.like_icon.source = "images/liked.png"

    def like(self):
        if self.liked:
            self.ids.like_icon.source = "images/like.png"
            if self.comment_id:
                '''r = requests.delete(
                    "https://lifehealther.onrender.com/content_like/delete/" +
                    str(self.content_id) + "/" + str(self.customer_id))'''
            self.liked = False
        else:
            self.ids.like_icon.source = "images/liked.png"
            if self.comment_id:
                '''data = {
                    "content_id": int(self.content_id),
                    "customer_id": int(self.customer_id)
                }
                r = requests.post("https://lifehealther.onrender.com/content_like/create", json=data)'''
            self.liked = True