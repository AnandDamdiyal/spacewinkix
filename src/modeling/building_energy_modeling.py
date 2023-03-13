import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class BuildingEnergyModel:
    def __init__(self, data_file):
        self.data_file = data_file
    
    def load_data(self):
        df = pd.read_csv(self.data_file)
        return df
    
    def prepare_data(self, df):
        # drop unnecessary columns
        df = df.drop(['building_id'], axis=1)
        # split into training and testing data
        X = df.drop(['energy_consumption'], axis=1)
        y = df['energy_consumption']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        return X_train, X_test, y_train, y_test
    
    def train_model(self, X_train, y_train):
        # train a linear regression model
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model
    
    def evaluate_model(self, model, X_test, y_test):
        # evaluate the model
        r2 = model.score(X_test, y_test)
        return r2
    
    def predict_energy_consumption(self, model, data):
        # make predictions for new data
        predictions = model.predict(data)
        return predictions
    
# example usage
if __name__ == '__main__':
    data_file = 'building_energy_data.csv'
    model = BuildingEnergyModel(data_file)
    df = model.load_data()
    X_train, X_test, y_train, y_test = model.prepare_data(df)
    trained_model = model.train_model(X_train, y_train)
    r2_score = model.evaluate_model(trained_model, X_test, y_test)
    print(f'R^2 score: {r2_score}')
