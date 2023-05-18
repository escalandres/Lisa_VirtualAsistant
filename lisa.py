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

def convertir_libras_a_pesos(libras):
    url = "https://api.exchangerate-api.com/v4/latest/GBP"  # API para obtener la tasa de cambio
    response = requests.get(url)
    data = response.json()
    tasa_cambio = data["rates"]["MXN"]  # Tasa de cambio de libras a pesos mexicanos

    pesos = libras * tasa_cambio
    return pesos

contactos = {
    'andrew':'+525545464585',
    'mom':'+525545460034',
    'jorge':'+56932739269'
}
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
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'are you there' in command:
        talk('Yes, I am here')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'alpha' in command:
        talk('Opening WolframAlpha')
        Wolfram()
    elif 'goodbye' in command:
        global close
        close=1
        talk('Okay')
    elif 'convert money' in command:
        # Ejemplo de uso
        talk("Enter the amount of British Pounds to convert into Mexican pesos")
        libras = float(input("British Pounds: "))
        pesos_mexicanos = convertir_libras_a_pesos(libras)
        print(f"{libras} British Pounds equals to {pesos_mexicanos} Mexican pesos.")
        talk(f"{libras} British Pounds equals to {pesos_mexicanos} Mexican pesos.")
    elif 'what is my internet speed' in command:
        st = speedtest.Speedtest()
        talk('I am checking your internet speed. Please give a minute')
        #velocidad de descarga
        d=st.download()
        d=(d*pow(10,-6)) #se hace la conversion de bits a megabits
        strdownload = format(d,".2f") #se convierte a dos decimales
        u=st.upload()
        u=(u*pow(10,-6))
        strupload = format(u,".2f")
        p=st.results.ping
        strping = str(p)
        #download
        print('Your download speed is: '+strdownload+' MB/s')
        talk('Your download speed is: '+strdownload+' Megabytes per second')
        #Velocidad de carga
        print('Your upload speed is: '+strupload+' MB/s')
        talk('Your upload speed is: '+strupload+' Megabytes per second')
        #El ping
        print('Your internet ping is: '+strping+' ms')
        talk('Yor internet ping is: '+strping+' miliseconds')
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
    elif 'send a message' in command:
        er=False
        talk('Ok, To whom do you want to send this message?')
        while er == False:
            try:
                name=take_command()
                if 'to' in name:
                    name=name.replace('to','')
                elif 'two' in name:
                    name=name.replace('two','')
                receiver=contactos[name]
                er=True
            except:
                print("I didn't understand you. Please repeat it again")
                talk("I didn't understand you. Please repeat it again")
        talk('Ok, what do you want to send to '+name+'?')
        message=get_info()
        h = datetime.datetime.now().strftime('%H')
        hour=int(h)
        mi = datetime.datetime.now().strftime('%M')
        minute=int(mi)+1
        print('Message to'+name+' = '+receiver+' at '+h+':'+mi)
        print('OK, your message will be sent in one minute. Please wait!')
        talk('OK, your message will be sent in one minute. Please wait!')
        pywhatkit.sendwhatmsg(receiver,message,hour,minute)
        #pywhatkit.sendwhatmsg(contactos['Tere'],"This is a message",17,10)
        talk('Ok, your message has been sent to '+name)
    elif 'show me the camera' in command:
        print('Opening camera...')
        talk('Ok, opening camera')
        os.system('python security_camera.py')
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