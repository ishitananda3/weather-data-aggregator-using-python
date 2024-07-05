
import requests
import json

API_KEY = ''
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather_data(api_key,location):
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == '__main__':
    data = fetch_weather_data('London')
    print(json.dumps(data, indent=4))
