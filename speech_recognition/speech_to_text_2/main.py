


# https://www.youtube.com/watch?v=LSdT1kRZh1k

# https://github.com/Abhishek-op/SR/blob/main/Speechrecognizer/platforms/android/stt.py

# https://pypi.org/project/SpeechRecognition/

# https://groups.google.com/g/kivy-users/c/urdqLafmeEQ

# https://www.youtube.com/watch?v=LSdT1kRZh1k



from kivy.config import Config
Config.set('kivy','keyboard_mode','systemanddock')


from kivy.app import App

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

import speech_recognition as sr

# Properties
from kivy.properties import ObjectProperty


# Define our differeent screens
class MainWindow(Screen):

    command_text = ObjectProperty(None)
    
    def getaudio(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            audio = r.listen(source)
        self.audio = audio

        try:
            self.command_text.text = str(r.recognize_google(audio, language="de"))

        except sr.UnknownValueError:
            self.command_text.text = "Did not understand audio"
        
        except sr.RequestError as e:
            self.command_text.text = str(f"Error: {e}")








# https://github.com/kivymd/KivyMD/wiki/Modules-Material-App#exceptions
class BasicApp(App):
    def __init__(self, **kwargs):
        self.title = "Sail Commander App"
        super().__init__(**kwargs)

    def build(self):
        # Load file function musst be in build and not before
        kv = Builder.load_file("speech_to_text.kv")
        self.root = kv


if __name__ == "__main__":
    BasicApp().run()

