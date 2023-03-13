import pandas as pd
import numpy as np

class CarbonEmissionsDataProcessor:
    def __init__(self, data_path):
        self.data_path = data_path
        
    def process_data(self):
        """
        Processes carbon emissions data to extract useful features
        """
        # Load data
        emissions_df = pd.read_csv(self.data_path)
        
        # Filter for relevant columns
        emissions_df = emissions_df[["Country Name", "Country Code", "Year", "CO2 emissions (kt)"]]
        
        # Rename columns for readability
        emissions_df.columns = ["Country", "Code", "Year", "CO2_Emissions"]
        
        # Convert CO2_Emissions to numeric data type
        emissions_df["CO2_Emissions"] = pd.to_numeric(emissions_df["CO2_Emissions"], errors="coerce")
        
        # Drop rows with missing values
        emissions_df.dropna(inplace=True)
        
        # Group by country and year and calculate average CO2 emissions
        emissions_df = emissions_df.groupby(["Country", "Year"]).agg({"CO2_Emissions": np.mean}).reset_index()
        
        return emissions_df
