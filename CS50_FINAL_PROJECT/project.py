import sys
import requests
import pyfiglet
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

base_url = "https://api.openweathermap.org/data/2.5/weather"
def get_api():
    api = "6dd4c9cf8ca04055ae86bf099ede112e"
    return api

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

def get_weather_data(city):
    url = f"{base_url}?q={city}&appid={get_api()}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

def format_weather_data(data,city):
    icon = data["weather"][0]["icon"]
    weather_icon = WEATHER_ICONS.get(icon, "")
    country = data["sys"]["country"]
    display = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
    formatted_data = {
        "display": display,
        "description": data["weather"][0]["description"].title(),
        "weather_icon": weather_icon,
        "latitude": data['coord']['lat'],
        "longitude": data['coord']['lon'],
        "temperature": data['main']['temp'],
        "feels_like": data['main']['feels_like'],
        "max_temp": data['main']['temp_max'],
        "min_temp": data['main']['temp_min'],
        "humidity": data['main']['humidity'],
        "pressure": data['main']['pressure'],
        "wind_speed": data['wind']['speed']
    }
    return formatted_data

def main():
    city = input('Enter city: ')
    data = get_weather_data(city)
    if data is None:
        print(f'{Fore.RED} Error: Unable to retrieve weather information.')
        sys.exit()

    formatted_data = format_weather_data(data,city)
    print (f"{Fore.GREEN}{Style.BRIGHT}=================================== WEATHER REPORT ===================================")
    print(f'{Fore.CYAN} {Style.BRIGHT} {formatted_data["display"]}')
    print(f"{Fore.YELLOW} {Back.BLACK} {Style.BRIGHT} {formatted_data['description']}{formatted_data['weather_icon']}")
    print()
    print(f"{Fore.GREEN} {Style.BRIGHT} LATITUDE-> {formatted_data['latitude']}     LONGITUDE-> {formatted_data['longitude']}\n")
    print(f"{Fore.RED} {Style.BRIGHT}           Temperature: {formatted_data['temperature']}°C 🌡️ ")
    print(f"{Fore.CYAN} {Style.BRIGHT}           Feels Like:  {formatted_data['feels_like']}°C 🌡️ ")
    print(f"{Fore.YELLOW} {Style.BRIGHT}           Max Temp:    {formatted_data['max_temp']}°C 🥵 ")
    print(f"{Fore.YELLOW} {Style.BRIGHT}           Min Temp:    {formatted_data['min_temp']}°C 🥶 ")
    print(f"{Fore.MAGENTA} {Style.BRIGHT}           Humidity:    {formatted_data['humidity']}% 💧")
    print(f"{Fore.BLUE} {Style.BRIGHT}           Pressure:    {formatted_data['pressure']} millibars 🌪️ ")
    print(f"{Fore.WHITE} {Style.BRIGHT}           Wind Speed:  {formatted_data['wind_speed']} m/s 💨 ")
    print (f"{Fore.GREEN}{Style.BRIGHT}=======================================================================================")


if __name__ == "__main__":
    main()
