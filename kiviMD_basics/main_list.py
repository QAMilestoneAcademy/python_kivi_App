from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem

class DemoApp(MDApp):
    def build(self):
        screen=MDScreen()
        item1=OneLineListItem(text='Item 1')
        return screen