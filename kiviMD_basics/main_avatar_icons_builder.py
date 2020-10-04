from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
#Flow to Icon/Avatar list : IconLeftWidget/IconRightWidget -> OneLineListItem-> MDList -> ScrollView -> Screen

list_helper='''
MDScreen:
    ScrollView:
        MDList:
            id:container  
'''
class DemoApp(MDApp):
    def build(self):
        screen=Builder.load_string(list_helper)

        return screen
    def on_start(self):
        for i in range(20):
            items=OneLineListItem(text='item ' + str(i))
            self.root.ids.container.add_widget(items)
DemoApp().run()