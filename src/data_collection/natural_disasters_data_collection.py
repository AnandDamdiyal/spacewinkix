import requests
import pandas as pd

class NaturalDisasterDataCollector:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/"
        
    def collect_earthquakes_data(self, start_date, end_date):
        """
        Collects earthquake data for a specific time range
        """
        # Set parameters
        endpoint = "earthquakes"
        params = {
            "start": start_date,
            "end": end_date,
            "orderby": "magnitude",
            "minmagnitude": 4.5,
            "format": "geojson",
            "limit": 1000,
            "apikey": self.api_key
        }
        
        # Make API request
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        
        # Check for errors
        if response.status_code != 200:
            raise ValueError(f"Error: {response.status_code}")
            
        # Convert response to pandas dataframe
        earthquakes_df = pd.read_json(response.text, orient="columns")
        
        return earthquakes_df
    
    def collect_hurricanes_data(self, start_date, end_date):
        """
        Collects hurricane data for a specific time range
        """
        # Set parameters
        endpoint = "cylone"
        params = {
            "start": start_date,
            "end": end_date,
            "format": "geojson",
            "limit": 1000,
            "apikey": self.api_key
        }
        
        # Make API request
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        
        # Check for errors
        if response.status_code != 200:
            raise ValueError(f"Error: {response.status_code}")
            
        # Convert response to pandas dataframe
        hurricanes_df = pd.read_json(response.text, orient="columns")
        
        return hurricanes_df
