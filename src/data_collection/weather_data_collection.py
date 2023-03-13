import requests
import pandas as pd

class WeatherDataCollector:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/"
        
    def collect_current_weather(self, city, country_code):
        """
        Collects current weather data for a specific city and country
        """
        # Set parameters
        endpoint = "weather"
        params = {
            "q": f"{city},{country_code}",
            "appid": self.api_key
        }
        
        # Make API request
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        
        # Check for errors
        if response.status_code != 200:
            raise ValueError(f"Error: {response.status_code}")
            
        # Convert response to pandas dataframe
        weather_df = pd.read_json(response.text, orient="columns")
        
        return weather_df
    
    def collect_forecast_weather(self, city, country_code):
        """
        Collects weather forecast data for a specific city and country
        """
        # Set parameters
        endpoint = "forecast"
        params = {
            "q": f"{city},{country_code}",
            "appid": self.api_key
        }
        
        # Make API request
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        
        # Check for errors
        if response.status_code != 200:
            raise ValueError(f"Error: {response.status_code}")
            
        # Convert response to pandas dataframe
        weather_df = pd.read_json(response.text, orient="columns")
        
        return weather_df
