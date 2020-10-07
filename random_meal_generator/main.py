from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.label import Label
import requests
import webbrowser
#https://themealdb.com/api.php
#https://www.themealdb.com/api/json/v1/1/random.php
class HomeScreen(Screen):
    pass
class MainApp(MDApp):
    MealName = StringProperty()
    MealCategory = StringProperty()
    Origin = StringProperty()
    MealImage = StringProperty()
    MealSource = StringProperty()
    url = 'https://www.themealdb.com/api/json/v1/1/random.php'
    def __init__(self, **kwargs):
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = "Orange"
        Window.size = (400, 600)
        super().__init__(**kwargs)
        # self.MealName=StringProperty()
        # self.MealCategory=StringProperty()
        # self.Origin=StringProperty()
        # self.MealImage=StringProperty()
        # self.MealSource=StringProperty()

    def on_start(self):
        ingredient_list=self.root.ids['home'].ids['ingredient_list']
        url='https://www.themealdb.com/api/json/v1/1/random.php'
        recipe=requests.get(url).json()
        # print("MealName",recipe['meals'][0]['strMeal'])
        # print("MealCategory", recipe['meals'][0]['strCategory'])
        # print("Origin", recipe['meals'][0]['strArea'])
        # print("Meal Image", recipe['meals'][0]['strMealThumb'])
        # print("Meal Source", recipe['meals'][0]['strSource'])
        self.MealName=recipe['meals'][0]['strMeal']
        self.MealCategory=recipe['meals'][0]['strCategory']
        self.Origin=recipe['meals'][0]['strArea']
        self.MealImage=recipe['meals'][0]['strMealThumb']
        if recipe['meals'][0]['strSource']!=None:
         self.MealSource= recipe['meals'][0]['strSource']
        else:
            self.MealSource =""
        for i in range(1,21):
            if recipe['meals'][0][f'strIngredient{i}'] !="":
                l=Label(text=recipe['meals'][0][f'strIngredient{i}'],color=(1,1,1,1))
                ingredient_list.add_widget(l)

    def view(self):
        if self.MealSource!='':
         webbrowser.open_new(self.MealSource)
        else:
            Snackbar(text='Source is not available').show()

MainApp().run()