from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField

class DemoApp(MDApp):
    def build(self):
        screen=MDScreen()
        # username=MDTextField(text='Enter username', pos_hint={'center_x':0.5,'center_y':0.5},size_hint=(0.5,1))
        username=MDTextField(text='Enter username', pos_hint={'center_x':0.5,'center_y':0.5},size_hint_x=None,width=300)

        screen.add_widget(username)
        return screen

DemoApp().run()