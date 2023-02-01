import os
import pyttsx3
import speech_recognition as sr

class IDSD:
    def user_input(self):
        repeat = 2
        while repeat > 1:
            voice = sr.Recognizer()
            with sr.Microphone() as source:
                voice.pause_threshold = 0.5
                user_audio = voice.listen(source)
                try:
                    voice_ip = voice.recognize_google(user_audio, language='en-in')
                    print(voice_ip)
                except Exception as e:
                    if e:
                        repeat = 0
                    else:
                        repeat = 2
                try:
                    return voice_ip
                except Exception:
                    repeat = 2

    def comp_vc(self, audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()

    def work(self):
        rep = 2
        while rep > 1:
            task = self.user_input()
            choice = task
            #if "immediate" or "shut" or "down" or "shutdown" or "Shut" or "down" or " media" in choice:
            if "00" or "Zero" or "ZERO" or "zero" in choice:
                self.comp_vc("Shutting down the computer in T minus 3 seconds")
                os.system(f'shutdown /s /t 30')
                rep = 0


if __name__ == '__main__':
    obj = IDSD()
    obj.work()