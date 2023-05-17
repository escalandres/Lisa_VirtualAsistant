import speedtest
import os
import datetime
import pyttsx3
st=speedtest.Speedtest()
# import speech_recognition as sr
# listener = sr.Recognizer()
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# def talk(text):
#     engine.say(text)
#     engine.runAndWait()

# with sr.Microphone() as source:
#     talk('I am listening...')
#     print('listening...')
#     voice = listener.listen(source, phrase_time_limit=3)
#     command = listener.recognize_google(voice)
#     command = command.lower()
#     print(command)

# k=15+1
#print(k+1)

print(st.download())
print(st.upload())
print(st.results.ping)

#path_to_encrypt= os.path.expanduser('~')
#print(path_to_encrypt)
# hour = datetime.datetime.now().strftime('%H')

# minute = datetime.datetime.now().strftime('%M')
# print(type(hour))