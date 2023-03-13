import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

class NaturalDisasterDataProcessor:
    def __init__(self, data_file):
        self.data_file = data_file
    
    def load_data(self):
        """
        Loads natural disaster data from a CSV file and converts to pandas dataframe
        """
        data = pd.read_csv(self.data_file)
        return data
    
    def preprocess_data(self, data):
        """
        Preprocesses natural disaster data by normalizing and clustering
        """
        # Select relevant columns
        cols = ['year', 'disaster_type', 'affected_population']
        data = data[cols]
        
        # Normalize affected population
        scaler = MinMaxScaler()
        data['affected_population'] = scaler.fit_transform(data['affected_population'].values.reshape(-1, 1))
        
        # One-hot encode disaster type
        data = pd.get_dummies(data, columns=['disaster_type'])
        
        # Cluster the data into 3 groups
        kmeans = KMeans(n_clusters=3, random_state=0).fit(data)
        data['cluster'] = kmeans.labels_
        
        return data
