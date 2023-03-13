import pandas as pd
import numpy as np

class EnergyDemandDataProcessor:
    def __init__(self):
        pass
    
    def preprocess_data(self, energy_data):
        """
        Preprocesses the energy demand data for analysis
        """
        # Rename columns
        energy_data.rename(columns={"usage": "energy_demand"}, inplace=True)
        
        # Convert timestamp to datetime
        energy_data["timestamp"] = pd.to_datetime(energy_data["timestamp"])
        
        # Resample to hourly frequency
        energy_data = energy_data.set_index("timestamp")
        energy_data = energy_data.resample("H").sum()
        
        # Fill missing values with median
        energy_data["energy_demand"].fillna(energy_data["energy_demand"].median(), inplace=True)
        
        # Calculate moving averages
        energy_data["energy_demand_ma"] = energy_data["energy_demand"].rolling(window=24).mean()
        
        # Calculate differences
        energy_data["energy_demand_diff"] = energy_data["energy_demand"] - energy_data["energy_demand"].shift(1)
        
        return energy_data
