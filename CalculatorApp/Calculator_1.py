from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout=BoxLayout(orientation='horizontal')
            for label in row:
                button=Button(text=label,pos_hint={"center_x": 0.5, "center_y": 0.5})
                # button.bind(self.on_press_button)
                h_layout.add_widget(button)

            main_layout.add_widget(h_layout)
        equals_button = Button(
                text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
            )
        #equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)
        return main_layout


if __name__ == '__main__':
    app = CalculatorApp()
    app.run()