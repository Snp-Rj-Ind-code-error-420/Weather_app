from setting import *
import json,time,requests
city_name='jamshedpur'

API_Endpoint=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
API_Endpoint_metric=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"
API_Endpoint_forcast=f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_key}"
def prn():
	#Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit
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
	print(f'main={data['weather'][0]['main']}')
	print(f'city {data['name']},{data['sys']['country']}')
	print()
	sunrise=time.localtime(data['sys']['sunrise'])
	print(f'sunrise {sunrise[2]}/{sunrise[1]}/{sunrise[0]} {sunrise[3]}:{sunrise[4]}:{sunrise[5]} ')
	sunset=time.localtime(data['sys']['sunset'])
	print(f'sunrise {sunset[2]}/{sunset[1]}/{sunset[0]} {sunset[3]}:{sunset[4]}:{sunset[5]} ')
	print()
	x=time.localtime(data['dt'])
	print(f'date = {data['dt']} {time.localtime(data['dt'])}\n {x[2]}/{x[1]}/{x[0]} {x[3]}:{x[4]}:{x[5]} ')
	x=time.gmtime(data['dt'])
	print(f'date = {data['dt']} {time.gmtime(data['dt'])}\n {x[2]}/{x[1]}/{x[0]} {x[3]}:{x[4]}:{x[5]} ')


def pull(city_nam):
	print('ok run it ')
	API_Endpoint_metric=f"https://api.openweathermap.org/data/2.5/weather?q={city_nam}&appid={API_key}&units=metric"
	response = requests.get(API_Endpoint_metric)
	print(response.status_code)
	if response.status_code==429:
		print('api request limit crossed')
		return 
	if response.status_code==404:
		print('error not found wtf you looking for')
		return
	if response.status_code==401:
		print('Unauthorise api wtf you change the api code or what')
		return
	if response.status_code==400:
		print('your request parametr is fucking wrong')
		return


	data = response.json()
	return data

if __name__=='__main__':
	print(API_Endpoint) # api url not be leaked anywhere in the program 

	print(API_Endpoint_forcast) # api url not be leaked anywhere in the program 

	response = requests.get(API_Endpoint)
	print(response.status_code)
	print(type(response.status_code))
	data = response.json()
	print(data)
	prn()

	response = requests.get(API_Endpoint_metric)
	print(response.status_code)
	data = response.json()
	print(data)
	prn()

# response = requests.get(API_Endpoint_forcast)
# print(response.status_code)
# data = response.json()
# print(data)

# print(data2)

