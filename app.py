api_key='ceeaeeaeb5b4db689ee714336c6ad8a7'

import requests
user_input=input('Enter city:')

weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")
if weather_data.json()['cod'] == 404:
    print('No city found')
else:
     weather =weather_data.json()['weather'][0]["main"]
     temp=weather_data.json()['main']['temp']
     print(f'The weather in {user_input} is {weather}')
     print(f'The temperature in {user_input} is {temp} Celsius')
