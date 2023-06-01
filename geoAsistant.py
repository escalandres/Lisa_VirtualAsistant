import wolframalpha
app_id = "RGKTU7-VYTGGTHK2Y"
client = wolframalpha.Client(app_id)
import speedtest 
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import PySimpleGUI as sg
import os
sg.theme('DarkAmber')
from gtts import gTTS
import datetime
#import security_camera
import requests

#-----------------------------------------------------------------------------------------
#Declaracion de funciones
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Adjusting for background noise. One second")
            listener.adjust_for_ambient_noise(source)
            talk("Ok, I'm listening to you")
            print('listening...')
            voice = listener.listen(source, phrase_time_limit=10)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'lisa' in command:
                command = command.replace('lisa', '')
            print(command)
    except LookupError:   # speech is unintelligible
        print("Could not understand audio")
        pass
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    except Exception as e:
        print("Error:", e)
    except:
        print('Goodbye')
    return command

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source,phrase_time_limit=15)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def Wolfram():
    layout =[[sg.Text('Enter a math operation'), sg.InputText()],[sg.Button('Ok'), sg.Button('Cancel')]]
    #operation=sg.InputText()
    window = sg.Window('PyDa', layout)
    event, values = window.read()
    try:
        wolfram_res = next(client.query(values[0]).results).text
        talk("Wolfram Result: "+wolfram_res)
        sg.PopupNonBlocking("Wolfram Result: "+wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say("Wikipedia Result: "+wiki_res)
        sg.PopupNonBlocking("Wikipedia Result: "+wiki_res)
    engine.runAndWait()
    window.close()

def run_alexa():
    command = take_command()
    print('Procesing your request...')
    talk('Procesing your request')
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        print('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print('Current time is: ' + time +'.')
    elif 'president' in command:
        person = command
        wolfram_res = next(client.query(person).results).text
        talk(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk('wikipedia result:'+info)
    elif 'goodbye' in command:
        global close
        close=1
        talk('Okay')
    elif 'search for' in command:
        search = command.replace('search for', '')
        pywhatkit.search(search)
    elif 'take note' in command:
        try:
            with sr.Microphone() as source:
                path_to_save='C:\\Users\\Andres Escala\\Desktop'
                talk("Okay, I'm listening to you...")
                print('listening...')
                note = listener.listen(source)
                voiceNote = listener.recognize_google(note)
                voiceNote = voiceNote.lower()
                #'en': 'English', 'es': 'Spanish', 'ja': 'Japanese', 'de': 'German', 'zh-CN': 'Chinese'
                tts = gTTS(text=voiceNote, lang='en', slow=False) 
                x=datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
                tts.save(f''+path_to_save+'\\'+"voiceNote_{x}.mp3")
                tts.save(f''+path_to_save+'\\'+"voiceNote_{x}.txt")
        except:
            pass
    else:
        talk('Please say the command again.')

#-----------------------------------------------------------------------------------------#
#Condigo principal
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
close=0
talk('Hi, I\'m Lisa. How can I help?...')
while True:
    run_alexa()
    if close == 1:
        talk('See you again. Have a nice day')
        break
    talk('Do you need anything else?...')
    print('Do you need anything else?...')