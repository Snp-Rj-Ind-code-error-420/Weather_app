from setting import *
import json
import requests
city_name='jamshedpur'

API_Endpoint=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"

print(API_Endpoint)

response = requests.get(API_Endpoint)
print(response.status_code)
data = response.json()
print(data)