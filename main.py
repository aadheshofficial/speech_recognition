import speech_recognition as sr
from vosk import Model, KaldiRecognizer
import json

r = sr.Recognizer()
# for offline speech recognition download vosk model and unzip in the name of 'model'
# https://alphacephei.com/vosk/models

def listen_online():
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
        r.adjust_for_ambient_noise(source)
        try:
            message = r.recognize_google(audio_text)          
            print("Text: "+message)
        except:
            message = "unabe to recognize"
            print(message)
        return message
    
def listen_offline():
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
        r.adjust_for_ambient_noise(source)
        try:
            message = r.recognize_vosk(audio_text) 
            data = json.loads(message)
            message = data.get('text','')          
            print("Text: "+message)
        except:
            message = "unabe to recognize"
            print(message)
        return message


if __name__ == '__main__':
    # listen_offline()
    listen_online()