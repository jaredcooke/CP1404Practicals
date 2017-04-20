from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Jared Cooke'

class MileToKm(App):
    def build(self):
        Window.size = (500, 200)
        self.title = "Convert Mile to Kilometres"
        self.root = Builder.load_file('mile_to_km.kv')
        return self.root

    def handle_increment(self, value):
        current = self.root.ids.input_number.text
        try:
            new = float(current) + value
        except ValueError:
            new = value
        self.root.ids.input_number.text = str(new)

    def handle_convert(self):
        miles = self.root.ids.input_number.text
        try:
            km = float(miles) * 1.60934
            self.root.ids.output_label.text = str(round(km, 3))
        except ValueError:
            self.root.ids.output_label.text = '0.0'

MileToKm().run()
