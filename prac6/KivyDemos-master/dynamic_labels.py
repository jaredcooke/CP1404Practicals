from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Label


class Dynamic_Labels(App):
    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super().__init__(**kwargs)
        self.strings = ['this', 'better', 'work']

    def build(self):
        Window.size = (500, 500)
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def create_widgets(self):
        for string in self.strings:
            temp_button = Label(text=string)
            #temp_button.bind(on_release=self.press_entry)
            self.root.ids.dynamic_box.add_widget(temp_button)

    def clear_widgets(self):
        self.root.ids.dynamic_box.clear_widgets()
Dynamic_Labels().run()