import speech_recognition as sr
from gtts import gTTS
import PyDictionary as pd
import os
 

r = sr.Recognizer()

def audio():
    print("Entered")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("entered microphone")
        audio = r.listen(source,timeout=3)
        voice_data = ""
        print("welcome")
        try:
            print("enter try block")
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            save('Sorry, I did not get that')
        except sr.RequestError:
            save("Sorry, my speech service is down")
        except:
            save('Sorry, some error occured')
        return voice_data

def save(audio_string):
    current = os.getcwd()
    os.chdir(current+'/static/')
    tts = gTTS(text=audio_string, lang='en')
    audio_file = 'audio.mp3'
    tts.save(audio_file)
    os.chdir(current)
    
        

def respond(voice_data):
    dictionary=pd.PyDictionary()
    if "meaning" in voice_data:
        data=voice_data.split(" ")
        data.remove('meaning')
        if len(data)==1:
            a=dictionary.meaning(data[0])
            for i in a.values():
                s=''
                for j in i:
                    s+=j
                save(s)
                return
        else:
            save('Sorry, I did not get that')
    elif "antonym" in voice_data:
        data=voice_data.split(" ")
        data.remove('antonym')
        if len(data)==1:
            a=dictionary.antonym(data[0])
            print(a)
            save(a[0])
        else:
            save('Sorry, I did not get that')
    elif "translate" in voice_data:
        data=voice_data.split(" ")
        data.remove('translate')
        if len(data)==1:
            a=dictionary.translate(data[0],'hi')
            print(a)
            save(a)
        else:
            save('Sorry, I did not get that')
            
                
              
def call():
    voice_data = audio()
    respond(voice_data)
    

