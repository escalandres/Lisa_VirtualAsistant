monicaToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIyIiwianRpIjoiMjMyMjQ2NWIzNGZjNmRmYWZhM2FhZDczM2NhYTdjOWU3OTQwZjZiMzFjMmQ1YzJmOWE5YzQwOGZlM2FlNWRjZDBiZThiNzllNzUyYWRmNGQiLCJpYXQiOjE2ODY1NDQ3NzQuNDMyNTY0LCJuYmYiOjE2ODY1NDQ3NzQuNDMyNTY2LCJleHAiOjE3MTgxNjcxNzQuNDI0NjE5LCJzdWIiOiIzNzI1NSIsInNjb3BlcyI6W119.oRB-WmHwT9CMyWuAn5zl1URXGi4Wqb-x2ixhLAcxhG1IL_COkRTnBXr2jMJGK88TaTLyqBpcdnT1irDekSdgCek6zphuJFFlK4Fygu8gSuWf9BqbX5BVV2Q1MxWJC3q_STf_BwHUmG971wIlzy0IlJDSfx8u7lZR2Iktoq21l9VSqDMV3rtHa40n7twhe8MbYOi-ybpF12ciV6nRljKNza2_Y2MktmBDuqENNRKZcBfmGdHQTqL0ncvMx4ps6rIwvDKMrwZkRQ8s5_EkeRf8WFqavLdgnozeiTUj4WXCtasj8Vz9sFZYzVPHCBPasRsvh9iCi8txHf5OZTmn0qDKYvsTOu401Z6D_sWyrjt2W99gLSJuoEEi5mWbIDTUTulQ6nKiJh-vGXI1wTZQyObybJ26yPk0dSuvWTw1LO6OItOz964PcV9Ca2N8trIIiDVnoaJ1hwJky4305y913sJH2mQwIUIbnZwMxaGeXswUqUCu_bBf3D0v9_265_p2MyAYBGAlnfRGbHo2qa-dOHvjbCD2R9KL-CruxDoHyiQ4TL3NytVKnRK0VbblnkMEK1znU_gsaTwe5obrAH_7dPRPgDHOpBAJB_2AHf8XW59w3QnIE2ztMha20GMbn5ZGB8DeRrkH932thsnMQm-T0szs5mmh4XS9KQ3qtX8neTSgbi4"
from monica import MonicaClient
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
import json
#pip install requests
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
    elif 'qué es' in command:
        search_term = command
        language = "es"
        wiki_wiki = wikipediaapi.Wikipedia(language)
        page = wiki_wiki.page(search_term)
        if page.exists():
            print("Título:", page.title)
            print("Contenido:", page.text)
        else:
            print("La página no existe.")

    elif 'oro' in command:
        url = "https://es.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "titles": "Oro",
            "exintro": True,
            "explaintext": True
        }
        response = requests.get(url, params=params)
        data = response.json()
        page = data["query"]["pages"].popitem()[1]
        print(page["extract"])
        talk(page["extract"])
    elif 'mónica' in command:
        try:
            # url = "https://app.monicahq.com/api"
            # texto = "Muestrame todas las propiedades del mineral mercurio"
            # payload = {'text': texto}
            # headers = {'Authorization': 'Token ' + monicaToken}

            # response = requests.post(url, headers=headers, data=payload)
            # data = json.loads(response.text)
            # sentimientos = data['sentiments']
            # entidades = data['entities']
            client = MonicaClient(access_token=monicaToken, api_url='https://app.monicahq.com/api')
            print(client.me)
            
        except Exception as e:
            print("Error:", e)
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
    