from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty
from kivymd.uix.dialog import MDDialog

class HomeScreen(Screen):
    weight=NumericProperty(40)
    def get_value(self):
        slider_height=self.ids.height_value.value

    def increase(self):
        self.weight=self.weight+1

    def decrease(self):
        self.weight=self.weight-1
    def calculate_bmi(self):
        #https://www.wikihow.com/Calculate-Your-Body-Mass-Index-(BMI)#:~:text=Divide%20your%20weight%20in%20kilograms,of%2024.5%20as%20your%20BMI.
        #BMI=weight/(height**2) kg/m2
        height=self.ids.height_value.value/100 #to convert to meter
        height_sq=height**2
        bmi=self.weight/height_sq
        # print(bmi)

        if bmi<18.5:
            weight_range="underweight"
        elif bmi>=18.5 and bmi<=24.9:
            weight_range ="normal"
        elif bmi>=25 and bmi<=29.9:
            weight_range ="overweight"
        else:
            weight_range ="obese"
        dialog=MDDialog(title='BMI',text='Your BMI is {}\nYour category is {}'.format(bmi,weight_range),size_hint=(.8,.3))
        dialog.open()
        # print("button pressed")


class MainApp(MDApp):
 def __init__(self):
     Window.size=(400,600)
     super().__init__()

MainApp().run()