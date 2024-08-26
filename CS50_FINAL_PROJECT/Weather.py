import sys
import requests
import pyfiglet
import colorama
from colorama import Fore,Back, Style
colorama.init(autoreset=True)

api = "6dd4c9cf8ca04055ae86bf099ede112e"
base_url = "https://api.openweathermap.org/data/2.5/weather"

WEATHER_ICONS = {
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧",
    "10d": "🌦",
    "11d": "⛈",
    "13d": "🌨",
    "50d": "🌫",

    "01n": "🌙",
    "02n": "☁️",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧",
    "10n": "🌦",
    "11n": "⛈",
    "13n": "🌨",
    "50n": "🌫",
}

city = input('Enter city: ')

url = f"{base_url}?q={city}&appid={api}&units=metric"

response = requests.get(url)
if response.status_code != 200:
    print (f'{Fore.RED} Error: Unable to retrieve weather information.')
    sys.exit()

data = response.json()
icon = data["weather"][0]["icon"]
weather_icon = WEATHER_ICONS.get(icon, "")
country = data["sys"]["country"]
display = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
print (f"{Fore.GREEN}{Style.BRIGHT}=================================== WEATHER REPORT ===================================")
print (f'{Fore.CYAN} {Style.BRIGHT} {display}')
print (f"{Fore.YELLOW} {Back.BLACK} {Style.BRIGHT} {data['weather'][0]['description'].title()}",weather_icon )
print ()
print (f"{Fore.GREEN} {Style.BRIGHT} LATITUDE-> {data['coord']['lat']}     LONGITUDE-> {data['coord']['lon']}\n")
print (f"{Fore.RED} {Style.BRIGHT}           Temperature: {data['main']['temp']}°C 🌡️ ")
print (f"{Fore.CYAN} {Style.BRIGHT}           Feels Like:  {data['main']['feels_like']}°C 🌡️ ")
print (f"{Fore.YELLOW} {Style.BRIGHT}           Max Temp:    {data['main']['temp_max']}°C 🥵 ")
print (f"{Fore.YELLOW} {Style.BRIGHT}           Min Temp:    {data['main']['temp_min']}°C 🥶 ")
print (f"{Fore.MAGENTA} {Style.BRIGHT}           Humidity:    {data['main']['humidity']}% 💧")
print (f"{Fore.BLUE} {Style.BRIGHT}           Pressure:    {data['main']['pressure']} millibars 🌪️ ")
print (f"{Fore.WHITE} {Style.BRIGHT}           Wind Speed:  {data['wind']['speed']} m/s 💨 ")

print (f"{Fore.GREEN}{Style.BRIGHT}=======================================================================================")
