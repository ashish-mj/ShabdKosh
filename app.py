from flask import Flask, render_template
from main import call
from pydub import AudioSegment
from pydub.playback import play
import os


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/intro')
def play_audio():
    current = os.getcwd()
    sound = AudioSegment.from_mp3(current+'/static/audio_intro.mp3')
    play(sound)
    return render_template('home.html')
    
    
@app.route('/speak')
def speak():
     call()
     current = os.getcwd()
     sound = AudioSegment.from_mp3(current+'/static/audio.mp3')
     play(sound)
     return render_template('home.html')    
 
@app.route('/help')
def help():
    current = os.getcwd()
    sound = AudioSegment.from_mp3(current+'/static/audio_help.mp3')
    play(sound)
    return render_template('home.html')   
    
if __name__=="__main__": 
    app.run(debug='False')
