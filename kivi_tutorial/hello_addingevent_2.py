#using kivi language
#Kivy will automatically look for a file that has the same name as the class in lowercase, without the App part of the class name.
#In this case, the class name is ButtonApp, so Kivy will look for a file named button.kv.
from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        return Button()

    def on_press_button(self):
        print('You pressed the button!')

if __name__=='__main__':
    app=ButtonApp()
    app.run()