import pandas as pd
import numpy as np

class RenewableEnergyProductionProcessor:
    def __init__(self, data_file):
        self.data_file = data_file
        
    def load_data(self):
        """
        Loads renewable energy production data from a CSV file
        """
        # Read CSV file
        data_df = pd.read_csv(self.data_file)
        
        # Convert date column to datetime format
        data_df["date"] = pd.to_datetime(data_df["date"])
        
        return data_df
    
    def preprocess_data(self, data_df):
        """
        Preprocesses renewable energy production data
        """
        # Add a year column
        data_df["year"] = data_df["date"].dt.year
        
        # Group data by year and calculate total energy production
        total_energy_df = data_df.groupby("year")["energy"].sum().reset_index()
        total_energy_df = total_energy_df.rename(columns={"energy": "total_energy"})
        
        # Group data by year and renewable energy source and calculate percentage of total energy
        renewable_energy_df = data_df.groupby(["year", "source"])["energy"].sum().reset_index()
        renewable_energy_df = renewable_energy_df.merge(total_energy_df, on="year")
        renewable_energy_df["percent_total"] = 100 * renewable_energy_df["energy"] / renewable_energy_df["total_energy"]
        
        return renewable_energy_df
    
    def predict_future_production(self, data_df):
        """
        Predicts future renewable energy production using linear regression
        """
        # Group data by year and calculate total energy production
        total_energy_df = data_df.groupby("year")["energy"].sum().reset_index()
        
        # Fit a linear regression model to the data
        X = total_energy_df["year"].values.reshape(-1, 1)
        y = total_energy_df["energy"].values.reshape(-1, 1)
        model = LinearRegression().fit(X, y)
        
        # Predict future energy production
        future_years = np.array(range(2022, 2051)).reshape(-1, 1)
        future_predictions = model.predict(future_years)
        future_predictions_df = pd.DataFrame({"year": future_years.reshape(-1), "energy": future_predictions.reshape(-1)})
        
        return future_predictions_df
