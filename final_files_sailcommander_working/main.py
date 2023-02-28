


# https://github.com/kivymd/KivyMD/blob/master/kivymd/icon_definitions.py
# Kivy MD
# https://www.youtube.com/watch?v=LRXo0juuTrw&list=PLhTjy8cBISEoQQLZ9IBlVlr4WjVoStmy-

from kivy.config import Config
Config.set('kivy','keyboard_mode','systemanddock')


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

scenario_commandos = sail_scenario()


class CommanderWindow(Screen):

    # pictures
    sail_png = ObjectProperty(None)
    wind_png = ObjectProperty(None)
    # scenarios
    sail_segel_up = ObjectProperty(None)
    sail_segel_down = ObjectProperty(None)
    sail_wende = ObjectProperty(None)
    sail_halse = ObjectProperty(None)
    # sail_mob = ObjectProperty(None)
    # actions
    command_text = ObjectProperty(None)
    send_command=ObjectProperty(None)
    delete_command=ObjectProperty(None)
    # Bitte Kommandos eingeben
    command_hints = ObjectProperty(None)
    arrow_left= ObjectProperty(None)
    arrow_right= ObjectProperty(None)
    # toggle
    # TODO:
    hints_onoff=ObjectProperty(None)
    # mic_onoff=ObjectProperty(None)


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

        self.show_wind_png()
        self.show_boat_png()

    def select_scenario(self, *args):
        scenario = self.get_scenario_selection()
        scenario_commandos.select_scenario(scenario)

    def clear_command(self, *args):
        self.command_text.text = ""

    def commando(self, *args):

        scenario = self.get_scenario_selection()


        try:
            # print(scenario_commandos.process_scenario(scenario=scenario, commando=self.command_text.text,segel=None, lage=None, wind=None))

            lower_text=self.command_text.text.lower()

            feedback, sail = scenario_commandos.process_scenario(scenario=scenario, commando=self.command_text.text,segel=None, lage=None, wind=boat_sail_info.get_wind() )

            if "fier auf" in lower_text:
                # print (lower_text)
                boat_sail_info.segel_lose()

                if boat_sail_info.get_wind() == "wind_90" or boat_sail_info.get_wind() == "wind_135" or boat_sail_info.get_wind() == "wind_225" or boat_sail_info.get_wind() == "wind_270":
                    feedback = "[fier auf ausgeführt]"

            if "hol dicht" in lower_text:
                # print (lower_text)
                boat_sail_info.segel_dichter()
                
                if boat_sail_info.get_wind() == "wind_90" or boat_sail_info.get_wind() == "wind_45" or boat_sail_info.get_wind() == "wind_270" or boat_sail_info.get_wind() == "wind_315":
                    feedback = "[hol dicht ausgeführt]"


            if sail is not None:
                boat_sail_info.update_segel(sail)

            # if feedback != "":
                # toast(feedback, duration=4)
            self.command_hints.text = feedback

            if (boat_sail_info.get_trim() == "rs") and (boat_sail_info.get_wind() == "wind_180"):
                print("Patenthalse")
                self.command_hints.text = "Autsch. Patenthalse"

            self.command_text.text = ""

        except ValueError:
            self.command_text.text = ""

        except AttributeError:
            self.command_text.text = ""


        self.show_boat_png()


    def get_scenario_selection(self, *args):

        if self.sail_segel_up.selected:
            return "Segel"
        if self.sail_segel_down.selected:
            return "Bergen"
        elif self.sail_wende.selected:
            return "Wende"
        elif self.sail_halse.selected:
            return "Halse"
    
    def commando_hint(self, *args):

        # TODO:

        if self.hints_onoff.state == "down":

            scenario = self.get_scenario_selection()

            self.command_text.text = scenario_commandos.hint_command(scenario=scenario)
        # pass








# button ansteuern
# output=str(self.mic_onoff.state)
# print(output)   #"normal", "down"

# output2=str(self.sail_wende.state)   # normal
# output2=str(self.sail_wende.selected)  #True, False
# print(output2) 





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

