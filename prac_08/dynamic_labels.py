"""
Kivy for CP1404, IT@JCU
Dynamically create buttons based on content of dictionary
Kevin Lui, 19/11/2024
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


COLOUR = (1, 0, 0, 1)  # RGBA for red


class DynamicLabelsApp(App):

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.index_to_name = {0: "Bob Brown", 1: "Kat Cyan", 2: "Owen Ochre", 3: "Kevin Lui"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from data and add them to the GUI."""
        for index, name in self.index_to_name.items():
            name_label = Label(text=name)
            name_label.background_color = COLOUR
            self.root.ids.main.add_widget(name_label)


DynamicLabelsApp().run()
