from tkinter import *
import time
import requests
import json
import swfuntion
import swengine
import playsound
root = Tk()
#root.after(time in millisecond, function name)
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.update()
root.attributes('-topmost', False)
ti = int(time.strftime("%H"))
root.configure(background='black')
root.lift()
#root.geometry("4000x3000")


def wakeup():
    swfuntion.swift_wake()


#####################################################################   Digital Clock App   #########################################################################
def times():
    current_time = time.strftime("%I:%M:%S %p")
    clock.config(text=current_time)
    clock.after(200, times)


def dates():
    if int(time.strftime("%d")) % 10 == 1:
        current_date = time.strftime("%d") + "st " + time.strftime("%B, %Y")
    elif int(time.strftime("%d")) % 10 == 1:
        current_date = time.strftime("%d") + "nd " + time.strftime("%B, %Y")
    elif int(time.strftime("%d")) % 10 == 1:
        current_date = time.strftime("%d") + "rd " + time.strftime("%B, %Y")
    else:
        current_date = time.strftime("%d") + "th " + time.strftime("%B, %Y")

    date.config(text=current_date)
    date.after(200, times)


photo = PhotoImage(file='/Users/sagnikchakraborty/Documents/Swift/images/askme.png')
myButton = Button(root, image=photo, command=wakeup, pady=0, padx=0, borderwidth=0, highlightthickness=0)
myButton.place(x=1750, y=820)
ti = int(time.strftime("%H"))
if 4 <= ti < 12:
    msg = "Good Morning"
elif 12 <= ti <= 18:
    msg = "Good Afternoon"
else:
    msg = "Good Evening"

massage = Label(root, text=msg, font=("Arial", 45), bg="black", fg="white")
massage.place(x=850, y=180)

clock = Label(root, font=("Arial", 200, "bold"), bg="black", fg="white")
clock.place(x=450, y=250)
times()

date = Label(root, font=("Arial", 80), bg="black", fg="white")
date.place(x=700, y=500)
dates()


#####################################################################   Weather App   #########################################################################
def city_name():
    res = requests.get('https://ipinfo.io/')
    data = res.json()
    city = data['city']
    location = data['loc'].split(',')
    latitude = location[0]
    longitude = location[1]
    # API Call
    api_request = requests.get("http://api.openweathermap.org/data/2.5/weather?q="
                               + city + "&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric")

    api = json.loads(api_request.content)

    # Temperatures
    y = api['main']
    current_temprature = y['temp']
    humidity = y['humidity']
    tempmin = y['temp_min']
    tempmax = y['temp_max']
    current_temprature = int(current_temprature)

    # Coordinates
    x = api['coord']
    longtitude = x['lon']
    latitude = x['lat']

    # Country
    z = api['sys']
    country = z['country']
    citi = api['name']
    citi = citi + ","

    # Adding the received info into the screen
    lable_temp.configure(text=current_temprature)
    lable_humidity.configure(text=humidity)
    max_temp.configure(text=tempmax)
    min_temp.configure(text=tempmin)
    lable_country.configure(text=country)
    lable_citi.configure(text=citi)


# Country  Names and Coordinates
lable_citi = Label(root, text="...", width=0,
                   fg="white", bg="black", font=("bold", 25))
lable_citi.place(x=110, y=133)

lable_country = Label(root, text="...", width=0,
                      fg="white", bg="black", font=("bold", 25))
lable_country.place(x=210, y=133)

# Current Temperature
if 4 <= ti < 12:
    img = PhotoImage(file="/Users/sagnikchakraborty/Documents/Swift/images/morningsun.png")
elif 12 <= ti <= 18:
    img = PhotoImage(file="/Users/sagnikchakraborty/Documents/Swift/images/noonsun.png")
else:
    img = PhotoImage(file="/Users/sagnikchakraborty/Documents/Swift/images/moon.png")

panel = Label(root, image=img, pady=0, padx=0, borderwidth=0, highlightthickness=0)
panel.place(x=200, y=190)

lable_temp = Label(root, text="...", width=0,
                   font=("Helvetica", 110), fg="white", bg="black")
lable_degree = Label(root, text="°C", width=0,
                     font=("Helvetica", 20), fg="white", bg="black")

lable_temp.place(x=58, y=190)
lable_degree.place(x=180, y=210)

# Other temperature details

humi = Label(root, text="Humidity: ", width=0,
             fg="white", bg="black", font=("bold", 15))
humi.place(x=113, y=370)

lable_humidity = Label(root, text="...", width=0,
                       fg="white", bg="black", font=("bold", 15))
lable_humidity.place(x=238, y=370)

maxi = Label(root, text="Max. Temp.: ", width=0,
             fg="white", bg="black", font=("bold", 15))
maxi.place(x=113, y=400)

max_temp = Label(root, text="...", width=0,
                 fg="white", bg="black", font=("bold", 15))
max_temp.place(x=238, y=400)

mini = Label(root, text="Min. Temp.: ", width=0,
             fg="white", bg="black", font=("bold", 15))
mini.place(x=113, y=430)

min_temp = Label(root, text="...", width=0,
                 fg="white", bg="black", font=("bold", 15))
min_temp.place(x=238, y=430)
city_name()
#####################################################################   Weather App   #########################################################################
playsound.playsound('/Users/sagnikchakraborty/Documents/Swift/audio/WELCOME.mp3')
swengine.talk(msg)
root.mainloop()
