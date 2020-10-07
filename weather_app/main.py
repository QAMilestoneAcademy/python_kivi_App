from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from bs4 import BeautifulSoup


import requests

class HomeScreen(Screen):
    weather=StringProperty()
    description = StringProperty()
    humidity = StringProperty()
    pressure = StringProperty()
    visibility = StringProperty()
    def search(self):
        city_name=self.ids.city_name.text
        print(city_name)
        country_name = self.ids.country_name.text
        print(country_name)
        url=f'https://www.timeanddate.com/weather/{country_name}/{city_name}'
        # sec_url='https://www.timeanddate.com/weather/united-arab-emirates/dubai'
        # response=requests.get(sec_url)
        response = requests.get(url)
        soup=BeautifulSoup(response.text,'html.parser')
        main_class=soup.find(class_='bk-focus__qlook')
        self.weather=main_class.find(class_='h2').get_text()
        # print(self.weather)
        self.description=main_class.find('p').get_text()
        # print(self.description)
        info_class=soup.find(class_="table table--left table--inner-borders-rows")
        th_list=info_class.find_all('tr')
        self.visibility =th_list[3].get_text()[11:]
        # print(self.visibility[11:])
        self.pressure=th_list[4].get_text()[8:17]
        # print(self.pressure[8:])
        self.humidity = th_list[5].get_text()[11:]
        # print(self.humidity[11:])



class MainApp(MDApp):
    def __init__(self,**kwargs):
        self.theme_cls=ThemeManager()
        self.theme_cls.theme_style='Dark'
        self.theme_cls.primary_palette = "LightBlue"
        #self.theme_cls.accent_color = "Black"
        Window.size=(400,600)
        super().__init__(**kwargs)


MainApp().run()