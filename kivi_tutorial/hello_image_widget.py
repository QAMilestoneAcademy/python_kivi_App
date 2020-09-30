from kivy.app import App
from kivy.uix.image import Image

class MainApp(App):
    def build(self):
        img = Image(source='sampleimage.jpg',
                    size_hint=(0.25, .25),
                    pos_hint={'center_x':.75, 'center_y':.2})

        return img

if __name__ == '__main__':
    app = MainApp()
    app.run()