import requests
import pandas as pd

class TransportationDataCollector:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.data.gov/nhtsa/"
        
    def collect_vehicle_data(self, make, model, year):
        """
        Collects vehicle data for a specific make, model, and year
        """
        # Set parameters
        endpoint = "SafetyRatings/modelyear"
        params = {
            "make": make,
            "model": model,
            "year": year,
            "format": "json"
        }
        
        # Make API request
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        
        # Check for errors
        if response.status_code != 200:
            raise ValueError(f"Error: {response.status_code}")
            
        # Convert response to pandas dataframe
        vehicles_df = pd.read_json(response.text, orient="columns")
        
        return vehicles_df
    
    def collect_fuel_data(self, model, year):
        """
        Collects fuel economy data for a specific vehicle model and year
        """
        # Set parameters
        endpoint = "webapi/api/vehicles"
        params = {
            "model": model,
            "year": year,
            "format": "json"
        }
        
        # Make API request
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        
        # Check for errors
        if response.status_code != 200:
            raise ValueError(f"Error: {response.status_code}")
            
        # Convert response to pandas dataframe
        fuel_df = pd.read_json(response.text, orient="columns")
        
        return fuel_df
