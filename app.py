

import requests
from dotenv import load_dotenv

import os

load_dotenv()
api_key=os.getenv("API_KEY")
if not api_key:
     print("Error:API key not found . Please set API_KEY in .env file")
     exit()


user_input=input('Enter city:')

weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")
weather_json=weather_data.json()
if weather_json['cod'] == 404:
    print('No city found')
else:
     weather =weather_json['weather'][0]["description"]
     temp=weather_json['main']['temp']
     feels_like=weather_json['main']['feels_like']

     print(f'The weather in {user_input} is {weather}')
     print(f'The temperature in {user_input} is {temp} Celsius')
     print(f'The weather feels like {feels_like}')
    
           