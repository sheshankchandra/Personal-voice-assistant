import smtplib
import datetime
import pyttsx3 
import speech_recognition as sr
import webbrowser
import os
import wikipedia
import pywhatkit as kt
import requests
import json
import pyjokes
from geopy import distance
from geopy.geocoders import Nominatim
from instabot import Bot
#by installing above python packages i have started working 


#creating a voice engine (sapi5:  API(application programming interface) developed by Microsoft to allow the use of speech recognition)
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')   
engine.setProperty('voice',voices[1].id)  #selecting a voice from the dictonary of voices 

#creating speak function 
def speak(audio):
    engine.say(audio)                   #speak output
    engine.runAndWait()   

def wishme():
    t=int(datetime.datetime.now().hour)
    if t>=0 and t<12:
        speak('Good morning buddy!')
    elif t>=12 and t<=18:
        speak('Good afternoon buddy')
    else:
        speak('Good evening buddy!')

    speak('How may I help you?')

def command():
    #we are taking the input from microphone and return output in string format
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold=3000
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def weather(city):
    api_key='f5a0d96512e244a5a561b6e7d88f4445'
    base_url='https://api.weatherbit.io/v2.0/current'
    #city='srikakulam'
    complete_url=base_url +'?&city='+city+'&key='+api_key+'&include=minutely'
    response = requests.get(complete_url)
    x=response.json()
    y=x["data"]
    z=y[0]
    s1='In current location '+z["city_name"]+'\n'+"the temperature is around "+str(z["temp"])+'celcius'+'\n'+'and'+z["weather"]["description"]
    speak(s1)

def location(city1):
    url1='https://www.google.com/maps/place/'+city1
    webbrowser.open(url1)

def directions(place1,place2):
    url2='https://www.google.com/maps/dir/'+place1+'/'+place2
    webbrowser.open(url2)

def places(place):
    url3='https://www.google.com/maps/search/'+place
    webbrowser.open(url3)

def distances(location1,location2):
    geocoder=Nominatim(user_agent='its me')
    location11=location1
    location22=location2
    coordinates1=geocoder.geocode(location11)
    coordinates2=geocoder.geocode(location22)
    lat1,long1=(coordinates1.latitude),(coordinates1.longitude)
    lat2,long2=(coordinates2.latitude),(coordinates2.longitude)
    place1=(lat1,long1)
    place2=(lat2,long2)
    d=distance.distance(place1,place2)
    speak(d)
    speak('this is the distance to reach the destination by flight')

def insta():
    bot=Bot()
    bot.login(username='give username',password='type password')
    speak('you logged in to instagram')

def send_mail(reciever,msg):
    #creating a server to send the mail
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    sender='enter your email_id'
    server.login(sender,'type password')
    server.sendmail(sender,reciever,msg)


if __name__=='__main__':
    wishme()
    while True:
        query=command().lower()

        if 'how are you' in query:
            speak("I'm fine")
        
        elif 'who are you' in query:
            speak("My name is auito. I'm your personal voice assistant")

        elif 'open google' in query:
            webbrowser.open('google.com')
        
        elif 'youtube' in query:
            webbrowser.open('youtube.com')

        elif 'amazon' in query:
            webbrowser.open('amazon.in')
        
        elif 'netflix' in query:
            webbrowser.open('netflix.in')
        
        elif 'spotify' in query:
            webbrowser.open('spotify.in')
        
        elif 'code' in query:
            os.startfile("C:\\Users\\neera\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        
        elif 'time' in query:
            t=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Now the time is {t}')
        
        elif 'wikipedia' in query:
            speak('searching wikipedia')
            query=query.replace('wikipedia','')
            res=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            speak(res)
        
        elif 'find' in query:
            query=query.replace('find','')
            kt.search(query)
        
        elif 'play' in query:
            query=query.replace('play','')
            speak('playing')
            kt.playonyt(query)
        
        elif 'weather' in query:
            try:
                speak('In which location')
                city=command().lower()
                weather(city)
            except:
               speak('an error occured')

        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        elif 'locate' in query:
            city1=query.replace('locate','')
            location(city1)
        
        elif 'directions' in query:
            speak('from which location')
            try:
                place1=command().lower()
                speak('please say the destination')
                place2=command().lower()
                directions(place1,place2)
            except:
                speak('an error occured')
        
        elif 'nearby' in query:
            place=query.replace('nearby','')
            places(place)
        
        elif 'instagram' in query:
            webbrowser.open('instagram.com')

        elif 'distance' in query:
            try:
                speak('from which location')
                location1=command().lower()
                speak('to which location')
                location2=command().lower()
                distances(location1,location2)
            except:
                speak('location does not exist')

        elif 'login' in query:
            insta()
        
        elif 'send mail' in query:
            try:
                speak('please type the reciever email address')
                reciever=str(input())
                speak('please say the msg to send')
                msg=command().lower()
            except:
                speak('an error occured')
                
        elif 'exit' in query:
            speak('Thanks for your time')
            exit()