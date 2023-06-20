from kivy.uix.button import Button
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp


class SubPreview(Button):
    def __init__(self, sponsor_tier_id, name='Subscription',
                 info='Text', price=0, subbed=False, **kwargs):
        super(SubPreview, self).__init__(**kwargs)
        self.sponsor_tier_id = sponsor_tier_id
        self.ids.name.text = name
        self.ids.description.text = info
        self.ids.price.text = str(price)+'$'
        self.subbed = subbed
        self.dialog = None
        if self.subbed:
            self.ids.sub_button.opacity = 0
            self.ids.sub_button.disabled = True
        else:
            self.ids.unsub_button.opacity = 0
            self.ids.unsub_button.disabled = True

    def sub(self):
        title = "Subscribe for " + self.ids.price.text + "?"
        if not self.dialog:
            self.dialog = MDDialog(
                title=title,
                buttons=[
                    MDRoundFlatButton(text="Cancel", on_release=self.close_popup),
                    MDRoundFlatButton(text="Yes", on_release=self.subscribe),
                ],
            )
        self.dialog.open()

    def close_popup(self, instance):
        self.dialog.dismiss()

    def subscribe(self, instance):
        self.close_popup(0)
        self.ids.sub_button.opacity = 0
        self.ids.sub_button.disabled = True
        self.ids.unsub_button.opacity = 1
        self.ids.unsub_button.disabled = False
        self.subbed = True
        # MDApp.get_running_app().sm.get_screen('creator').load_all_info()
        ...

    def unsub(self):
        title = "Unsubscribe?"
        if not self.dialog:
            self.dialog = MDDialog(
                title=title,
                buttons=[
                    MDRoundFlatButton(text="Cancel", on_release=self.close_popup),
                    MDRoundFlatButton(text="Yes", on_release=self.unsubscribe),
                ],
            )
        self.dialog.open()

    def unsubscribe(self, instance):
        self.close_popup(0)
        self.ids.sub_button.opacity = 1
        self.ids.sub_button.disabled = False
        self.ids.unsub_button.opacity = 0
        self.ids.unsub_button.disabled = True
        ...
