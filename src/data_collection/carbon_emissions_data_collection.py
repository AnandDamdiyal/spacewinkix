import requests
import pandas as pd

class CarbonEmissionsDataCollector:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.data.gov/eia/"
        
    def collect_emissions_data(self, state_abbr):
        """
        Collects carbon emissions data for a specific state
        """
        # Set parameters
        endpoint = "emissions/state"
        params = {
            "state": state_abbr,
            "api_key": self.api_key
        }
        
        # Make API request
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        
        # Check for errors
        if response.status_code != 200:
            raise ValueError(f"Error: {response.status_code}")
            
        # Convert response to pandas dataframe
        emissions_df = pd.read_json(response.text, orient="columns")
        
        return emissions_df
    
    def collect_energy_data(self, state_abbr):
        """
        Collects energy production data for a specific state
        """
        # Set parameters
        endpoint = "electricity/state"
        params = {
            "state": state_abbr,
            "api_key": self.api_key
        }
        
        # Make API request
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        
        # Check for errors
        if response.status_code != 200:
            raise ValueError(f"Error: {response.status_code}")
            
        # Convert response to pandas dataframe
        energy_df = pd.read_json(response.text, orient="columns")
        
        return energy_df
