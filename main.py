from tkinter import *
import requests
from tkinter import messagebox
import json
from datetime import datetime


window = Tk()
window.title("Weather Application")
window.minsize(width=550,height=550)
window.config(padx=30,pady=30)
bg = PhotoImage(file="image.png")
label1 = Label(window, image= bg)
label1.pack()

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()

def get_weather():
    api_key = "3c91f2ad78ccc17451c13dd68f107148"
    city_name = input_entry_1.get()
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key
    response = requests.get(weather_url)
    weather_info = response.json()
    if weather_info["cod"] == 200:
        kelvin = 273 #value of Kelvin

        temp = int(weather_info['main']['temp'] - kelvin)  # converting default kelvin value to Celcius
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nWind Speed: {wind_speed} k/h\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"

    else:
        messagebox.showinfo(title="Error",message="Please enter valid City Name!!")

    result_text.insert(INSERT,weather)

def reset():
    input_entry_1.delete(0,"end")
    result_text.delete(1.0,END)


my_label1 = Label(text="Enter the city:",font=("Times", 18 ,"normal"))
my_label1.pack()
input_entry_1 = Entry(width=41)
input_entry_1.pack()
my_button_1 = Button(window,text="Check Weather",command=get_weather,width=13)
my_button_1.pack()
weather_now = Label(text="The Weather is:",font=("Arial",20,"bold"))
weather_now.pack()
result_text = Text(width=54, height=15)
result_text.pack()
my_button_2 = Button(window,text="Reset",command=reset,width=13)
my_button_2.pack()

window.mainloop()