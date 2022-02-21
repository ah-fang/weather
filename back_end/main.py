from functions import *
from creds import open_weather_key


# api_path = api_configuration(32, 117, open_weather_key)
# print(api_path)
# payload = call_data(api_path)
# extract_json(payload)

creds = open_weather_key
city_id = '5386053' # san diego, CA


address = 'http://api.openweathermap.org/data/2.5/weather'
query = {'id': city_id, 'appid': creds}
response = requests.get(address, params=query)
print(response.json())


# City Name
# weather description
# feel like temp f
# High Temp in f
# Low Temp in f
# wind speed
# humidty
# longitude coordinates
# latitude coordinates
