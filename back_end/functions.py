import requests

def call_data(api_path):
    print('Attempt to call API')
    payload = requests.get(api_path)
    print(payload.json())
    return payload.json()


# def api_configuration(lat, lon, creds):
#     schema = 'http://'
#     address = 'api.openweathermap.org/data/2.5/weather'
#     customizable_parameteres = '?lat=' + str(lat) + '&lon=' + str(lon) + '&appid=' + creds
#     api_path = schema + address + customizable_parameteres
#     return api_path

def api_configuration(city_id, creds):
    schema = 'http://api.openweathermap.org/data/2.5/weather'
    address = ''
    query = {'id': city_id, 'appid': creds}


    # '?id={city id}&appid={API key}'



def extract_json(payload):
    data_longitude = payload['coord']['lon']
    data_latitude = payload['coord']['lat']

    print(data_latitude)