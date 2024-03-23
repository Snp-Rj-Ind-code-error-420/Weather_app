from setting import *
import json
import requests
city_name='jamshedpur'

API_Endpoint=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
API_Endpoint_metric=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"
API_Endpoint_forcast=f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_key}"
print(API_Endpoint)
print(API_Endpoint_forcast)



response = requests.get(API_Endpoint)
print(response.status_code)
data = response.json()
print(f'temperature {data['main']['temp']}')
print(f'temperature relative to human {data['main']['feels_like']}')
print(f'minimum temperature {data['main']['temp_min']}')
print(f'maximum temperature {data['main']['temp_max']}')
print()
print(f'pressure {data['main']['pressure']}') # hPa
print(f'humidity % {data['main']['humidity']}') # %
print()
print(f'visibility {data['visibility']}') # meters /1000 to km
print()
#Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour
print(f'wind speed {data['wind']['speed']}')
print()
print(f'cloud % {data['clouds']['all']}%') # %
print()

response = requests.get(API_Endpoint_metric)
print(response.status_code)
data = response.json()
print(f'temperature {data['main']['temp']}')
print(f'temperature relative to human {data['main']['feels_like']}')
print(f'minimum temperature {data['main']['temp_min']}')
print(f'maximum temperature {data['main']['temp_max']}')
print()
print(f'pressure {data['main']['pressure']}') # hPa
print(f'humidity % {data['main']['humidity']}') # %
print()
print(f'visibility {data['visibility']}') # meters /1000 to km
print()
#Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour
print(f'wind speed {data['wind']['speed']}')
print()
print(f'cloud % {data['clouds']['all']}%') # %
print()
# response = requests.get(API_Endpoint_forcast)
# print(response.status_code)
# data2 = response.json()
# print(data)
#Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit

# print(data2)

