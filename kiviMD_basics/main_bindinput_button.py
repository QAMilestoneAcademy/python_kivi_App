
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from helpers import username_helper

class DemoApp(MDApp):
    def build(self):
        screen=MDScreen()
        self.theme_cls.primary_palette="Blue"
        self.username=Builder.load_string(username_helper)
        button=MDRectangleFlatButton(text='Show',pos_hint={'center_x':0.5,'center_y':0.4},on_release=self.show_data)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen
    def show_data(self,obj):
        print(self.username.text)

DemoApp().run()