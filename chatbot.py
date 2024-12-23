import speech_recognition as sr
import os
import pyttsx3
import win32com.client


speaker = win32com.client.Dispatch("SAPI.SpVoice")


while 1:
    print("Enter the word you want to speak it out by computer")
    s = input()
    speaker.Speak(s)
1   


engine = pyttsx3.init()
engine.say("Hello richa")
engine.runAndWait()
