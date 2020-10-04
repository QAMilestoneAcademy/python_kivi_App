from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList,ThreeLineIconListItem,ThreeLineAvatarIconListItem
from kivymd.uix.list import IconLeftWidget,ImageRightWidget
from kivy.uix.scrollview import ScrollView

class DemoApp(MDApp):
    def build(self):
        screen=MDScreen()
        list_view=MDList()
        scroll = ScrollView()
        # item1=OneLineListItem(text='Item 1')
        # item2 =OneLineListItem(text='Item 2')
        # list_view.add_widget(item1)
        # list_view.add_widget(item2)
        for i in range(20):

            # icon=IconLeftWidget(icon='android')
            # items = ThreeLineIconListItem(text='Item ' + str(i), secondary_text='Hello World',tertiary_text='third text')
            image=ImageRightWidget(source='my_avatar.png')
            items = ThreeLineAvatarIconListItem(text='Item ' + str(i), secondary_text='Hello World',tertiary_text='third text')
            items.add_widget(image)
            list_view.add_widget(items)

        scroll.add_widget(list_view)
        screen.add_widget(scroll)
        return screen
DemoApp().run()