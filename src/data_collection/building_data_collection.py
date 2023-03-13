import requests
import pandas as pd

class BuildingDataCollector:
    def __init__(self, api_key):
        self.api_key = api_key
        
    def collect(self, city):
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}'
        response = requests.get(url)
        data = response.json()
        
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        clouds = data['clouds']['all']
        
        building_data = pd.DataFrame({'city': [city],
                                       'temperature': [temp],
                                       'humidity': [humidity],
                                       'pressure': [pressure],
                                       'wind_speed': [wind_speed],
                                       'cloud_cover': [clouds]})
        return building_data
