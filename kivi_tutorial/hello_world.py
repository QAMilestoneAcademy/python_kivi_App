# https://realpython.com/mobile-app-kivy-python/
from kivy.app import App
from kivy.uix.button import Button


class MainApp(App):
     def build(self):
        button = Button(text='Hello from Kivy',size_hint=(0.25,0.25),pos_hint={'center_x': .5, 'center_y': .5},background_color=[0,1,0,1])
        return button


if __name__ == '__main__':
    app = MainApp()
    app.run()
