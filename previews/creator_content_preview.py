from kivy.uix.button import Button
import requests

from update_article_screen import UpdateArticleScreen


class CreatorContentPreview(Button):
    def __init__(self, content_id,title, content_type, included, sub_id,  **kwargs):
        super(CreatorContentPreview, self).__init__(**kwargs)
        self.sub_id = sub_id
        self.content_id = content_id
        self.ids.title.text =title
        self.ids.type.text = content_type
        self.included = included
        #...
        if self.included:
            self.ids.add_button.opacity = 0
            self.ids.add_button.disabled = True
        else:
            self.ids.delete_button.opacity = 0
            self.ids.delete_button.disabled = True

    def delete(self):
        r = requests.delete("https://lifehealther.onrender.com/sponsor_tier_content/delete/" + str(self.sub_id) + "/" + str(self.content_id))

    def add(self):
        data = {
            "content": self.content_id,
            "sponsor_tier": self.sub_id
        }
        r = requests.post("https://lifehealther.onrender.com/sponsor_tier_content/create",json=data )
