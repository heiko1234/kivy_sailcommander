# import pyaudio
import speech_recognition as sr
# import pyttsx3
# from playsound import playsound
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.core.text import LabelBase



class MainWindow(Screen):
    # LabelBase.register(name='Roboto-Medium', 
    #                fn_regular='Roboto-Medium.ttf')
    def exit(self):
        quit()
        
class speechtotext(Screen):
    r = sr.Recognizer()
    # LabelBase.register(name='Roboto-Medium', 
    #                fn_regular='Roboto-Medium.ttf')
    
    def exit(self):
        quit()
    def change(self):
        self.ids.final_text.text = "Recognising"
        with sr.Microphone() as self.source:
            self.audio_data = self.r.listen(self.source)
            self.data = self.r.recognize_google(self.audio_data)
        
    def speechtotextfas(self):
                self.ids.final_text.text = self.data
            
    

kv = Builder.load_file("audiomain.kv")



class Audibuddy(App):
    
    def build(self):
        return kv
if __name__  ==  "__main__":
    Audibuddy().run()