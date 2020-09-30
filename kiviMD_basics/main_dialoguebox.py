# 1) Example of List - https://github.com/HeaTTheatR/KivyMD-data/raw/master/gallery/kivymddoc/lists.png
# 2) Create -> OneLineListItem
# https://raw.githubusercontent.com/HeaTTheatR/KivyMD-data/master/gallery/kivymddoc/lists.gif
#
# 3) Flow to create a list : OneLineListItem-> MDList -> ScrollView -> Screen
# 4) Create a for loop to add more items
# 5) Create a TwoLineListItem(secondary_text), ThreeLineListItem (tertiary_text)
#
# - Flow to Icon/Avatar list : IconLeftWidget/IconRightWidget -> OneLineListItem-> MDList -> ScrollView -> Screen
# 6) Add a OneLineIconListItem
# 7) Add a OneLineAvatarListItem
#
# 8) Use the Builder method to create a list
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
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
        if self.username.text is "":
            check_string='Please enter a user name'
        else:
            check_string = self.username.text + ' does not exist'

        close_button=MDFlatButton(text='Close',on_release=self.close_dialog)
        more_button = MDFlatButton(text='More')
        self.dialog=MDDialog(title='Username Check',text=check_string,size_hint=(0.5,1),buttons=[close_button,more_button])
        self.dialog.open()
        # print(self.username.text)
    def close_dialog(self,obj):
        self.dialog.dismiss()

DemoApp().run()