import requests
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class EnergyDemandModel:
    def __init__(self, api_key):
        self.api_key = api_key
        
    def collect_energy_data(self):
        # use requests library to fetch data from a free public API
        url = 'https://api.example.com/energydata'
        headers = {'Authorization': 'Bearer ' + self.api_key}
        response = requests.get(url, headers=headers)
        
        # convert response to pandas DataFrame
        energy_df = pd.DataFrame(response.json())
        
        return energy_df
    
    def preprocess_energy_data(self, energy_df):
        # drop unnecessary columns
        energy_df.drop(['date', 'hour'], axis=1, inplace=True)
        
        # split data into input (X) and output (y) variables
        X = energy_df.iloc[:, :-1].values
        y = energy_df.iloc[:, -1].values
        
        # split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        
        return X_train, X_test, y_train, y_test
    
    def train_energy_model(self, X_train, y_train):
        # train a linear regression model on the training data
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)
        
        return regressor
    
    def evaluate_energy_model(self, model, X_test, y_test):
        # make predictions on the testing data
        y_pred = model.predict(X_test)
        
        # calculate mean squared error
        mse = mean_squared_error(y_test, y_pred)
        
        return mse
