import os
from module_SDT import vi, ti


def SDF(n):
    os.system(f'shutdown /s /t {n}')

import pyttsx3
import speech_recognition as sr
import pyaudio


class SR:
    def take_input(self):
        var = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening")
            var.pause_threshold = 1
            audio = var.listen(source)
            try:
                print("Recognizing")
                voice_input = var.recognize_google(audio, language='en-in')
                print("your answer is {}".format(voice_input))
            except Exception as e:
                print(e)
                print("Repeat again")
                return "None"
            return voice_input

    def computer_voice(self, audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()

    def SDTimer(self):
        x = vi()
        self.computer_voice(x.__next__())
        take = self.take_input()
        choice = take
        if choice == "yes":
            self.computer_voice(x.__next__())
            time = int(self.take_input())
            print(time)
            y = ti(time)
            self.computer_voice(y.__next__())
            SDF(time)
        elif "execute" in choice:
            SDF(5)
        if choice == "no":
            print("Thanks")
            self.computer_voice("Thank you sir")


if __name__ == '__main__':
    mam = SR()
    mam.SDTimer()

# Basic cmds for pyttsx3 module
# import pyttsx3
# engine = pyttsx3.init() # object creation
#
# """ RATE"""
# rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
# engine.setProperty('rate', 125)     # setting up new voice rate
#
#
# """VOLUME"""
# volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)                          #printing current volume level
# engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
#
# """VOICE"""
# voices = engine.getProperty('voices')       #getting details of current voice
# #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
#
# engine.say("Hello World!")
# engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()
#
# """Saving Voice to a file"""
# # On linux make sure that 'espeak' and 'ffmpeg' are installed
# engine.save_to_file('Hello World', 'test.mp3')
# engine.runAndWait()