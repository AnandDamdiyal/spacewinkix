import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

class NaturalDisasterModel:
    def __init__(self, api_key):
        self.api_key = api_key
        
    def collect_data(self, data_source):
        # use requests library to get data from data source API
        response = requests.get(data_source)
        data = response.json()
        
        # convert data to pandas dataframe
        df = pd.DataFrame(data)
        return df
    
    def prepare_data(self, df):
        # select relevant features and convert to numeric values
        features = ['latitude', 'longitude', 'depth', 'mag']
        df = df[features]
        df = df.apply(pd.to_numeric, errors='coerce')
        
        # remove any rows with missing data
        df.dropna(inplace=True)
        return df
    
    def train_model(self, df):
        # split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(df.drop('mag', axis=1), df['mag'], test_size=0.3, random_state=42)
        
        # train linear regression model
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # evaluate model on testing data
        score = model.score(X_test, y_test)
        print(f"Model score: {score}")
        
        return model
    
    def visualize_results(self, df, model):
        # plot actual vs predicted magnitudes
        fig, ax = plt.subplots()
        ax.scatter(df['mag'], model.predict(df.drop('mag', axis=1)))
        ax.plot([df['mag'].min(), df['mag'].max()], [df['mag'].min(), df['mag'].max()], 'k--', lw=4)
        ax.set_xlabel('Actual')
        ax.set_ylabel('Predicted')
        plt.show()
