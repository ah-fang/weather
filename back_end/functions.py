import requests
import pandas as pd


def create_df():
    # creates the columns for the final df
    # needs to be outside the for loop so that it remembers it's values
    col1 = {
        'city': [
                    'weather_description',
                    'current_temp',
                    'feels_like',
                    'high_temp',
                    'low_temp',
                    'wind_speed',
                    'humidity',
                    'longitude',
                    'latitude']
    }
    df = pd.DataFrame(data=col1)
    return df


def call_open_weather(city_id, creds, units):
    # makes the api call and returns json file
    address = 'http://api.openweathermap.org/data/2.5/weather'
    query = {'id': city_id, 'appid': creds, 'units': units}
    response = requests.get(address, params=query)
    return response.json()


def extract_json(payload, df):
    # extract key info from json and add to df
    data_city = payload['name']
    data_weather_description = payload['weather'][0]['description']
    data_temp = payload['main']['temp']
    data_feel_temp = payload['main']['feels_like']
    data_high_temp = payload['main']['temp_max']
    data_low_temp = payload['main']['temp_min']
    data_humidity = payload['main']['humidity']
    data_wind_speed = payload['wind']['speed']
    data_longitude = payload['coord']['lon']
    data_latitude = payload['coord']['lat']

    df[data_city] = [data_weather_description,
                     data_temp,
                     data_feel_temp,
                     data_high_temp,
                     data_low_temp,
                     data_wind_speed,
                     data_humidity,
                     data_longitude,
                     data_latitude]