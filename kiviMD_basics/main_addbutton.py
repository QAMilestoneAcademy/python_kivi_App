
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton,MDIconButton,MDFloatingActionButton

class DemoApp(MDApp):
    def build(self):
        screen=MDScreen()
        # btn_flat = MDFlatButton(text='Hello World', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        btn_flat=MDRectangleFlatButton(text='Hello World',pos_hint={'center_x':0.3,'center_y':0.5})
        # btn_icon=MDIconButton(icon='lightbulb',pos_hint={'center_x':0.5,'center_y':0.5})
        btn_icon = MDFloatingActionButton(icon='lightbulb', pos_hint={'center_x': 0.5, 'center_y': 0.5})
        screen.add_widget(btn_icon)
        screen.add_widget(btn_flat)
        return screen

DemoApp().run()