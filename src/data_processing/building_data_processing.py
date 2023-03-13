import pandas as pd
import numpy as np

class BuildingDataProcessor:
    def __init__(self, buildings_df, energy_df):
        self.buildings_df = buildings_df
        self.energy_df = energy_df
        
    def clean_buildings_data(self):
        """
        Cleans the buildings data and removes unnecessary columns
        """
        self.buildings_df = self.buildings_df.dropna()
        self.buildings_df = self.buildings_df[["building_count", "total_site_energy", "total_source_energy"]]
        
    def clean_energy_data(self):
        """
        Cleans the renewable energy data and removes unnecessary columns
        """
        self.energy_df = self.energy_df.dropna()
        self.energy_df = self.energy_df[["station_name", "latitude", "longitude", "ev_network", "ev_level2_evse_num"]]
        
    def merge_dataframes(self):
        """
        Merges the buildings and renewable energy dataframes
        """
        self.buildings_df = self.buildings_df.rename(columns={"building_count": "num_buildings"})
        self.energy_df = self.energy_df.rename(columns={"ev_level2_evse_num": "num_ev_chargers"})
        self.data_df = pd.merge(self.buildings_df, self.energy_df, how="inner", left_index=True, right_index=True)
        
    def calculate_energy_efficiency(self):
        """
        Calculates energy efficiency metrics for the merged dataframe
        """
        self.data_df["site_energy_intensity"] = self.data_df["total_site_energy"] / self.data_df["num_buildings"]
        self.data_df["source_energy_intensity"] = self.data_df["total_source_energy"] / self.data_df["num_buildings"]
        self.data_df["ev_chargers_per_building"] = self.data_df["num_ev_chargers"] / self.data_df["num_buildings"]
        
    def get_top_locations(self, num_locations):
        """
        Returns the top locations based on energy efficiency metrics
        """
        self.top_locations = self.data_df.nsmallest(num_locations, "site_energy_intensity")[["latitude", "longitude"]]
        return self.top_locations
