from keys import api_key
import requests
import csv

city = 'Chicago'
state = 'Illinois'
country = 'US'


res = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={api_key}&units=imperial')
data = res.json()
# print(data['weather'][0]['main'])
# print(data['main']['temp'])
# print(data['wind']['speed'])

weather = data['weather'][0]['main']
temp = data['main']['temp']
wind_speed = data['wind']['speed']


print(f'Current weather in {city},{state}')
print('Sky: {}'.format(weather))
print('Temperature: {} Fahrenheit'.format(temp))
print('Wind: {} mph'.format(wind_speed))

