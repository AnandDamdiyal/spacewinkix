import requests
import pandas as pd

class TransportationDataProcessor:
    def __init__(self, api_key):
        self.api_key = api_key
        
    def collect_data(self, start_date, end_date, city):
        url = f"https://api.transport.com/v1/data?start_date={start_date}&end_date={end_date}&city={city}&apikey={self.api_key}"
        response = requests.get(url)
        
        if response.status_code != 200:
            print("Error: Failed to collect data from API")
            return None
        
        data = response.json()
        
        # Convert JSON data to Pandas DataFrame
        df = pd.DataFrame(data["data"])
        return df
    
    def preprocess_data(self, df):
        # Rename columns
        df = df.rename(columns={"Date": "date", "Hour": "hour", "Route": "route", "Passengers": "passengers"})
        
        # Convert date column to datetime
        df["date"] = pd.to_datetime(df["date"])
        
        # Remove any rows with missing values
        df = df.dropna()
        
        # Add a new column for total passengers
        df["total_passengers"] = df.groupby(["date", "hour"])["passengers"].transform("sum")
        
        return df
