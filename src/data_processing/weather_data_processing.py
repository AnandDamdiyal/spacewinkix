import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class WeatherDataProcessor:
    def __init__(self, weather_data):
        self.weather_data = weather_data
        
    def process_weather_data(self):
        """
        Processes raw weather data and returns a cleaned pandas dataframe
        """
        # Filter relevant columns
        relevant_cols = ["date_time", "temp", "precip"]
        weather_df = self.weather_data[relevant_cols].copy()
        
        # Convert date_time column to datetime format
        weather_df["date_time"] = pd.to_datetime(weather_df["date_time"])
        
        # Add new columns for year, month, and day
        weather_df["year"] = weather_df["date_time"].dt.year
        weather_df["month"] = weather_df["date_time"].dt.month
        weather_df["day"] = weather_df["date_time"].dt.day
        
        # Group by year, month, and day and calculate average temperature and total precipitation
        weather_summary = weather_df.groupby(["year", "month", "day"]).agg({"temp": np.mean, "precip": np.sum})
        weather_summary.reset_index(inplace=True)
        
        # Add new column for date in yyyy-mm-dd format
        weather_summary["date"] = weather_summary.apply(lambda row: datetime(row["year"], row["month"], row["day"]).strftime("%Y-%m-%d"), axis=1)
        
        return weather_summary
