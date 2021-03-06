from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList,OneLineListItem,TwoLineListItem,ThreeLineListItem
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
            # items=OneLineListItem(text='Item '+ str(i))
            # items = TwoLineListItem(text='Item ' + str(i), secondary_text='Hello World')
            items = ThreeLineListItem(text='Item ' + str(i), secondary_text='Hello World',tertiary_text='third text')
            list_view.add_widget(items)

        scroll.add_widget(list_view)
        screen.add_widget(scroll)
        return screen
DemoApp().run()