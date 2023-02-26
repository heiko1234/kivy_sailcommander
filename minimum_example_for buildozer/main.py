


# https://github.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py
# Kivy MD
# https://www.youtube.com/watch?v=LRXo0juuTrw&list=PLhTjy8cBISEoQQLZ9IBlVlr4WjVoStmy-


from kivymd.app import MDApp

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


# Properties
from kivy.properties import ObjectProperty

# Clock
from kivy.clock import Clock

# background Threading
from threading import Thread

# partial: funktions reverenz + parameter übergabe
from functools import partial


# Define our differeent screens
class WelcomeWindow(Screen):

    def entrance_button_behavior(self, *args):
        Clock.schedule_once(self.switch_to_second_view, 1)

    def switch_to_second_view(self, *args):
        self.manager.current = "commanderwindow"
        self.manager.transition.direction="left"




class CommanderWindow(Screen):

    pass




# https://github.com/kivymd/KivyMD/wiki/Modules-Material-App#exceptions
class SailCommanderApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Sail Commander App"
        super().__init__(**kwargs)

    def build(self):
        # Load file function musst be in build and not before
        kv = Builder.load_file("main.kv")
        self.root = kv


if __name__ == "__main__":
    SailCommanderApp().run()

