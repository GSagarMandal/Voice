import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random # generate random numbers
import wikipedia # acces phase data form wikipedia
import webbrowser # highlevel interphase displaying web-based
import time
import datetime # combination between date and time
import os # to remove and created files
import pyautogui # screenshot
import pyttsx3 #text to speech libery in python
import requests # http request
import smtplib # mail handeling
import urllib.request
import urllib.parse # handel url
import re
class person:
    name = ''
    def setName(self, name):
        self.name = name

class sagar:
    name = ''
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        engine_speak("Hello Sir! GoodMorning!")

    elif hour>=12 and hour<18:
        engine_speak("Hello Sir! GoodAfternoon!")   

    else:
        engine_speak("Hello Sir! GoodEvening!")  

    engine_speak("I am sisko.Please tell me how can I help you")  
r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", voice_data.lower()) # print what user said
        return voice_data.lower()

# get string and make a audio file to be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,80000000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(sagar_obj.name + ":", audio_string) # print what app said
    os.remove(audio_file) # remove audio file
    
def email(to, content):
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.ehlo()
      server.starttls()
      server.login('sagarkumar.das@tnu.in', 'S7o6u8v8i4k5#') #change id and pass
      server.sendmail('arpan.mukherjee@tnu.in', to, content)
      server.close()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        engine_speak("Hello Sir! Good Morning!")

    elif hour>=12 and hour<18:
        engine_speak("Hello Sir! Good Afternoon!")   

    else:
        engine_speak("Hello Sir! Good Evening!")  

    engine_speak("I am sisko . Please tell me how can I help you")      
def respond(voice_data):
    
         
    # greeting
    if there_exists(['hey','hi','hello']):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)  
    #  name
    if there_exists(["what is your name","what's your name","tell me your name"]):

        if person_obj.name:
            engine_speak(f"My name is {sagar_obj.name}, {person_obj.name}") #gets users name from voice input
        else:
            engine_speak(f"My name is {sagar_obj.name}. what's your name?") #incase you haven't provided your name.

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name) # remember name in person object
    
    if there_exists(["what is my name"]):
        engine_speak("Your name must be " + person_obj.name)
    
    if there_exists(["your name should be"]):
        sagar_name = voice_data.split("be")[-1].strip()
        engine_speak("okay, i will remember that my name is " + sagar_name)
        sagar_obj.setName(sagar_name) # remember name in sagar object

    #  greeting
    if there_exists(["how are you","how are you doing"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)

    #  time
    if there_exists(["what's the time","tell me the time","what time is it","what is the time"]):
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        engine_speak(f"Sir, the time is {strTime}")

    #  search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term)

    #  search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        search_term = search_term.replace("on youtube","").replace("search","")
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term)

     # get stock price
    if there_exists(["price of"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")
    
    
    
     # weather
    if there_exists(["weather"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")

     # toss a coin
    if there_exists(["toss","flip","coin"]):
        moves=["head", "tails"]   
        cmove=random.choice(moves)
        engine_speak("The computer chose " + cmove)
        
     # screenshot
    if there_exists(["capture","my screen","screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('D://pictures //screen.png')
        engine_speak("screenshot has been captured")
    
    
     # to search wikipedia for definition
    if there_exists(["wikipedia"]):
        search_term = voice_data.split("for")[-1]
        url = "https://en.wikipedia.org/w/index.php?search="+search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term)

    if there_exists(["exit", "quit", "goodbye","stop"]):
        engine_speak("bye! see you later")
        exit()
   
   
   # Current location as per Google maps
    if there_exists(["what is my exact location", "where am I"]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        engine_speak("You must be somewhere near here, as per Google maps")
    
    if there_exists(["play music"]):
        search_term = voice_data.split("for")[-1]
        url = "https://music.youtube.com/search?q="+ search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on youtubemusic")      
    
    if there_exists(["email", "mail"]):
        try:
                engine_speak("What should I say?")
                content = record_audio()
                to = "rj9832rj@gmail.com"    
                email(to, content)
                engine_speak("Email has been sent!")
        except Exception as e:
                print(e)
                engine_speak("Sorry sagar. I am not able to send this email")    

    if there_exists(["vs code"]):
        codePath = "C:\\Users\\sagar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        engine_speak("opening Visual Studio")
        os.startfile(codePath)
        
    if there_exists(["cmd"]):
        cmdPath = "C:\\WINDOWS\\System32\\cmd.exe"
        os.startfile(cmdPath)
        engine_speak("opening command prompt")
    
    if there_exists(["power off", "shut down"]):
        engine_speak("Do you want to shutdown your laptop")
        while True:
          command = record_audio()
          if "no" in command:
                engine_speak("Thank u sir I will not shut down the computer")
                break
          if "yes" in command:
        # Shutting down
                engine_speak("Shutting down the computer")
                os.system("shutdown /s /t 0")
                break    
              
    if there_exists(["restart"]):
        engine_speak("Do you want to restart your laptop")
        while True:
          command = record_audio()
          if "no" in command:
                engine_speak("Thank u sir I will not shut down the computer")
                break
          if "yes" in command:
        # Shutting down
                engine_speak("restarting the computer")
                os.system("shutdown /r /t 0")
                break   
            
person_obj = person()
sagar_obj = sagar()
sagar_obj.name = 'sisko'
person_obj.name = "sagar"
engine = pyttsx3.init()

wishMe()
while(1):
    voice_data = record_audio("Listening") # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data) # respond