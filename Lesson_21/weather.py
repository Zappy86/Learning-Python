import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print("\n***Get current weather conditions***\n")

    city = input("\nPlease enter a city name:\n")

    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial"

    weather_data = requests.get(request_url).json()
    
    print(f'\nCurrent weather for {weather_data["name"]}')
    print(f'\nTemp is {weather_data["main"]["temp"]} F')
    print(f'\nFeels like {weather_data["main"]["feels_like"]} F, with {weather_data["weather"][0]["description"].title()}')
    
    #pprint(weather_data)

if __name__ == "__main__":
    get_current_weather()