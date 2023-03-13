import requests
import pandas as pd

class NaturalDisasterMonitor:
    def __init__(self, api_key):
        self.api_key = api_key
        
    def get_earthquake_data(self, location):
        url = f"https://api.naturaldisasters.com/earthquake?location={location}&key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data['earthquake_data'])
        return df
        
    def get_hurricane_data(self, location):
        url = f"https://api.naturaldisasters.com/hurricane?location={location}&key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data['hurricane_data'])
        return df
        
    def get_wildfire_data(self, location):
        url = f"https://api.naturaldisasters.com/wildfire?location={location}&key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data['wildfire_data'])
        return df
