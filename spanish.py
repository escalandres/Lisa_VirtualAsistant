import wolframalpha
app_id = "RGKTU7-VYTGGTHK2Y"
client = wolframalpha.Client(app_id)
import speedtest 
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import wikipediaapi

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
    command = ""
    try:
        with sr.Microphone() as source:
            #print("Adjusting for background noise. One second")
            listener.adjust_for_ambient_noise(source)
            #talk("Ok, I'm listening to you")
            print('listening...')
            voice = listener.listen(source, phrase_time_limit=10)
            command = listener.recognize_google(voice, language="es-ES")
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
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
    print('Procesando tu petición...')
    talk('Procesando tu petición...')
    if 'reproduce' in command:
        song = command.replace('reproduce', '')
        print('Reproduciendo: ' + song)
        talk('Reproduciendo: ' + song)
        pywhatkit.playonyt(song)
    elif 'cuales son' in command:
        try:
            print(command)
            person = command
            wolfram_res = next(client.query(person).results).text
            talk(wolfram_res)
            sg.PopupNonBlocking(wolfram_res)
        except Exception as e:
            print("Error:", e)
    elif 'muéstrame más información sobre' in command:
        person = command.replace('muéstrame más información sobre', '')
        info = wikipedia.summary(person, 1)
        print('wikipedia result: '+info)
        talk('wikipedia result: '+info)
    elif 'que es' in command:
        search_term = command
        language = "es"
        wiki_wiki = wikipediaapi.Wikipedia(language)
        page = wiki_wiki.page(search_term)
        if page.exists():
            print("Título:", page.title)
            print("Contenido:", page.text)
        else:
            print("La página no existe.")
    elif 'adiós' or 'apagate' or 'hasta luego' in command:
        global close
        close=1
        talk('Okay')
    elif 'busca' in command:
        search = command.replace('busca', '')
        pywhatkit.search(search)
    else:
        talk('NO te entendí, ¿puedes repetirlo?')

#-----------------------------------------------------------------------------------------#
#Condigo principal
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[3].id)
close=0
os.system('cls' if os.name == 'nt' else 'clear')
talk('Hola, soy Alexa. ¿Cómo puedo ayudarte?')
while True:
    run_alexa()
    if close == 1:
        talk('¡Que tengas un buen día!')
        break
    print('¿Necesitas algo más?...')
    talk('¿Necesitas algo más?...')
    