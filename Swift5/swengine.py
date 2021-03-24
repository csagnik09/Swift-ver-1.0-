import os
import speech_recognition as sr
import playsound
from gtts import gTTS
import webbrowser
from tkinter import *
import requests
import osascript
import datetime


##############################################Swift Basic Skill Functions###########################################
# Convert Number in Words
def cttxt(innum):
    number = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    nty = ["", "", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninty"]
    tens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
            "Nineteen"]
    n = int(innum)
    if n > 99999:
        print("Cant solve for more than 5 digits")
    else:
        d = [0, 0, 0, 0, 0]
        i = 0
        while n > 0:
            d[i] = n % 10
            i += 1
            n = n // 10
        num = ""
        if d[4] != 0:
            if d[4] == 1:
                num += tens[d[3]] + " Thousand "
            else:
                num += nty[d[4]] + " " + number[d[3]] + " Thousand "
        else:
            if d[3] != 0:
                num += number[d[3]] + " Thousand "
        if d[2] != 0:
            num += number[d[2]] + " Hundred "
        if d[1] != 0:
            if d[1] == 1:
                num += tens[d[0]]
            else:
                num += nty[d[1]] + " " + number[d[0]]
        else:
            if d[0] != 0:
                num += number[d[0]]
        return num


# Tale input Using Swift
def input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        playsound.playsound('/Users/sagnikchakraborty/Documents/Swift/audio/POP.mp3')
        osascript.osascript("set volume output volume 10")
        audio_text = r.listen(source, phrase_time_limit=5)
        try:
            print("You: " + r.recognize_google(audio_text))
            osascript.osascript("set volume output volume 50")
            #playsound.playsound('/Users/sagnikchakraborty/Documents/Swift/audio/Done.mp3')
        except:
            osascript.osascript("set volume output volume 50")
            playsound.playsound('/Users/sagnikchakraborty/Documents/Swift/audio/RFAIL.mp3')
            print("Sorry, Please Trying Again..")
    return r.recognize_google(audio_text).lower()


# Output using swift
def talk(statement):
    tts = gTTS(text=statement, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


# Change volume using swift
def setvol(vol):
    vol = vol.replace("set volume to ", "")
    vol = int(vol)
    if int(vol) > 10:
        talk("To change volume choose between 0 and 10, for example say Set volume to 5")
    else:
        vol = vol * 10
        st = "set volume output volume " + str(vol)
        osascript.osascript(st)


# Shut Down Swift
def shutdown(self):
    talk("Quitting Swift")
    talk("Bye")
    talk("and if you are going out please wear a mask and be safe")
    sys.exit()


# Open Apps in Swift
def openinswift(name):
    open_name = name.replace("open ", "")
    talk("Are you sure you want to open" + open_name)
    act = input()
    if "yes" in act:
        if os.system('open -a' + open_name) == 0:
            talk("Done")
        else:
            talk("opening" + open_name + "in your browser")
            open_name = "https://www." + open_name + ".com"
            webbrowser.open(open_name, new=2)
    if "no" in act:
        talk("Ok, not opening " + open_name)


# Quit Apps in Swift
def quitinswift(name):
    close_name = name.replace("quit", "")
    talk("Are you sure you want to quit" + close_name)
    act = input()
    if "yes" in act:
        if os.system("killall" + " " + close_name.title()) == 0:
            talk("Done")
    if "no" in act:
        talk("Ok, not quitting " + close_name)


# Play Anything From Web
def play(topic):
    topic = topic.replace("play", "")
    url = 'https://www.youtube.com/results?q=' + topic
    count = 0
    cont = requests.get(url)
    data = str(cont.content)
    lst = data.split('"')
    for i in lst:
        count += 1
        if i == 'WEB_PAGE_TYPE_WATCH':
            break
    if lst[count - 5] == "/results":
        raise Exception("No video found.")

    webbrowser.open("https://www.youtube.com/" + lst[count - 5])
    talk("Playing " + topic)

# Stop Playing Music
def stopmusic(self):
    name = "Safari"
    close_name = name.replace("quit", "")
    if os.system("killall" + " " + close_name) == 0:
        talk("Done")


# System Date
def date(self):
    now = datetime.datetime.now()
    print("Current date is:  ")
    ydate = cttxt(now.strftime("%Y"))
    mdate = now.strftime("%B")
    ddate = cttxt(now.strftime("%d"))
    talk("Today is " + ddate + mdate + ydate)


# System Time
def sw_time(self):
    now = datetime.datetime.now()
    htime = cttxt(now.strftime("%H"))
    mtime = cttxt(now.strftime("%M"))
    stime = cttxt(now.strftime("%S"))
    talk("Now the time is " + htime + "hours and" + mtime + "minutes and" + stime + "seconds")


# Web Functions
def search_youtube(action):
    action = action.replace('search', '')
    action = action.replace(' for', '')
    action = action.replace(' on', '')
    action = action.replace(' youtube', '')
    webbrowser.open("https://www.youtube.com/results?search_query=" + action)
    talk("I found this on Youtube" + action)
    talk("check it out")


# Search on Web
def search_web(action):
    action = action.replace('search', '')
    action = action.replace(' for', '')
    action = action.replace(' on', '')
    action = action.replace(' web', '')
    lib = action
    url = "https://www.google.co.in/search?q=" + (str(lib)) + "&oq=" + (
        str(lib)) + "&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
    webbrowser.open_new(url)
    talk("I found this on google for" + action)
    talk("check it out")


# Weather Functions
def wehth(self):
    def weather_data(query):
        res = requests.get(
            'http://api.openweathermap.org/data/2.5/weather?' + query + '&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
        return res.json()

    def print_weather(result, city):
        talk("Currently {} is having temperature of {} degree centigrade".format(city, result['main']['temp']))

    def weather():
        res = requests.get('https://ipinfo.io/')
        data = res.json()
        city = data['city']
        location = data['loc'].split(',')
        latitude = location[0]
        longitude = location[1]
        query = 'q=' + city
        w_data = weather_data(query)
        print_weather(w_data, city)

    weather()


'''def sw_scrap(search):
    URL = "https://www.google.com/search?q={search}"
    req = requests.get(URL)
    sav = BeautifulSoup(req.text, "html.parser")
    update = sav.find("div", class_="BNeawe").text
    print(update)'''

##############################################Swift Basic Skill Functions###########################################
