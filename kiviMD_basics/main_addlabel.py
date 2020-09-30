#RGB color-https://www.w3schools.com/colors/colors_rgb.asp
#
# 1) theme_colors
# https://raw.githubusercontent.com/HeaTTheatR/KivyMD-data/master/gallery/kivymddoc/md-label-theme-text-color.png
#
# 2) Custom color
# 3) Styles
# https://raw.githubusercontent.com/HeaTTheatR/KivyMD-data/master/gallery/kivymddoc/md-label-font-style.gif
# 4) MDIcons
# https://github.com/HeaTTheatR/KivyMD/blob/master/kivymd/icon_definitions.py
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon

class DemoApp(MDApp):
    def build(self):
        label=MDLabel(text='Hello World', halign='center',theme_text_color='Custom',text_color=(6/255.0, 192/255.0, 174/255.0,1)
                      ,font_style='H1')
        icon_label=MDIcon(icon='leaf-maple',halign='center')
        return icon_label

DemoApp().run()