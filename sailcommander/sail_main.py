


# https://github.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py
# Kivy MD
# https://www.youtube.com/watch?v=LRXo0juuTrw&list=PLhTjy8cBISEoQQLZ9IBlVlr4WjVoStmy-


from kivymd.app import MDApp

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.toast.kivytoast.kivytoast import toast

from sail_class import sail_infos, sail_scenario


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

    # def on_enter(self, *args):
    #     # on_enter works automatically, while keyword
    #     Clock.schedule_once(self.switch_to_second_view, 3)

    def entrance_button_behavior(self, *args):
        Clock.schedule_once(self.switch_to_second_view, 1)

    def switch_to_second_view(self, *args):
        self.manager.current = "commanderwindow"
        self.manager.transition.direction="left"


# init the boat outside of Screen
boat_sail_info = sail_infos()




class CommanderWindow(Screen):

    # pictures
    sail_png = ObjectProperty(None)
    wind_png = ObjectProperty(None)
    # scenarios
    sail_wende = ObjectProperty(None)
    sail_halse = ObjectProperty(None)
    sail_mob = ObjectProperty(None)
    # actions
    command_text = ObjectProperty(None)
    send_command=ObjectProperty(None)
    delete_command=ObjectProperty(None)
    # Bitte Kommandos eingeben
    command_hints = ObjectProperty(None)
    arrow_left= ObjectProperty(None)
    arrow_right= ObjectProperty(None)
    # toggle
    hints_onoff=ObjectProperty(None)
    mic_onoff=ObjectProperty(None)


    # def on_enter(self, *args):
    #     # on_enter works automatically, while keyword
    #     Clock.schedule_once(self.switch_png_view, 3)

    # def switch_png_view(self, *args):
    #     self.sail_png.source = "assets/sails/sail_up_bb.png"


    # def show_toast(self, *args):
    #     if self.command_text.text == "Heiss":
    #         toast("Test Kivy Toast", duration=4)
    #         self.command_text.text = ""

    def show_boat_png(self, *args):
        output=boat_sail_info.get_sail_pic()
        self.sail_png.source = f"assets/sails/{output}"

    def show_wind_png(self, *args):
        output=boat_sail_info.get_wind_pic()
        self.wind_png.source = f"assets/wind/{output}"

    def left(self, *args):
        boat_sail_info.get_left()

        self.show_wind_png()
        self.show_boat_png()

    def right(self, *args):
        boat_sail_info.get_right()

        # button ansteuern
        # output=str(self.mic_onoff.state)
        # print(output)   #"normal", "down"

        # output2=str(self.sail_wende.state)   # normal
        # output2=str(self.sail_wende.selected)  #True, False
        # print(output2) 

        self.show_wind_png()
        self.show_boat_png()

    def commando(self, *args):

        self.command_hints.text=self.command_text.text 
        self.command_text.text = ""








# https://github.com/kivymd/KivyMD/wiki/Modules-Material-App#exceptions
class SailCommanderApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Sail Commander App"
        super().__init__(**kwargs)

    def build(self):
        # Load file function musst be in build and not before
        kv = Builder.load_file("SailCommander.kv")
        self.root = kv


if __name__ == "__main__":
    SailCommanderApp().run()

