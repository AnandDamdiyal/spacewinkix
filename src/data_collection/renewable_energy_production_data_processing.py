import pandas as pd
import requests

class RenewableEnergyProductionDataProcessor:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.eia.gov/"
        
    def get_renewable_energy_production_data(self, state_abbr):
        """
        Collects renewable energy production data for a specific state
        """
        # Set parameters
        endpoint = "series/"
        series_id = f"ELEC.GEN.REN.{state_abbr}-99.M"
        params = {
            "api_key": self.api_key,
            "series_id": series_id
        }
        
        # Make API request
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        
        # Check for errors
        if response.status_code != 200:
            raise ValueError(f"Error: {response.status_code}")
        
        # Convert response to pandas dataframe
        data = response.json()["series"][0]["data"]
        df = pd.DataFrame(data, columns=["Date", "Value"])
        df["Date"] = pd.to_datetime(df["Date"], format="%Y%m")
        df.set_index("Date", inplace=True)
        
        return df
    
    def calculate_renewable_energy_production_percentage(self, state_abbr):
        """
        Calculates the percentage of renewable energy production for a specific state
        """
        # Get renewable energy production data for the state
        renewable_df = self.get_renewable_energy_production_data(state_abbr)
        
        # Calculate total energy production
        total_production = renewable_df["Value"].sum()
        
        # Calculate renewable energy production percentage
        renewable_production = renewable_df.loc[renewable_df.index.year == 2021]["Value"].values[0]
        percentage = (renewable_production / total_production) * 100
        
        return percentage
