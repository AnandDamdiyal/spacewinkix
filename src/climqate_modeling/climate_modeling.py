import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

class ClimateModel:
    def __init__(self, data_file):
        self.data_file = data_file
    
    def train(self):
        data = pd.read_csv(self.data_file)
        
        # extract features and labels
        X = data.iloc[:, :-1].values
        y = data.iloc[:, -1].values
        
        # fit linear regression model
        model = LinearRegression()
        model.fit(X, y)
        
        self.model = model
    
    def predict(self, features):
        # convert features to numpy array and make prediction
        X = np.array([features])
        prediction = self.model.predict(X)
        
        return prediction[0]
