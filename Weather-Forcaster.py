import requests
import json
import win32com.client as wincom
import time

speak = wincom.Dispatch("SAPI.SpVoice")


print("Welcome to Weather Forecaster")

greet =  "Good Morning Dvanshu "
speak.Speak(greet)

time.sleep(0.05)
greeet = "Welcome to Weather Forecaster"
speak.Speak(greeet)
time.sleep(0.20)


greeet = "Please enter the name of city you want me to give weather forecast of"
speak.Speak(greeet)

city = input("Enter the name of city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=181a93e4f04742c7b2d00353233006&q={city}"

r = requests.get(url)
# print(r.text)

weather_dict = json.loads(r.text)

fcast = f'Todays weather in {city} is {weather_dict["current"]["condition"]["text"]} with a temperature of {weather_dict["current"]["temp_c"]}and Wind spead is {weather_dict["current"]["wind_kph"]} kilometer per hour and humidity is{weather_dict["current"]["humidity"]} percentage'

print(f'{weather_dict["current"]["condition"]["text"]}\n {weather_dict["current"]["temp_c"]}deg C\n{weather_dict["current"]["wind_kph"]}Kph\n{ weather_dict["current"]["humidity"]}%')


speak.Speak(fcast)


