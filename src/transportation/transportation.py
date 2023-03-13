import requests
import pandas as pd

class TransportationAnalyzer:
    def __init__(self, api_key):
        self.api_key = api_key
        
    def analyze_traffic(self, city):
        url = f"https://api.transportationdata.com/traffic?city={city}&key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data['traffic_data'])
        return df
        
    def optimize_route(self, origin, destination):
        url = f"https://api.transportationdata.com/route?origin={origin}&destination={destination}&key={self.api_key}"
        response = requests.get(url)
        data = response.json()
        optimized_route = data['optimized_route']
        return optimized_route
