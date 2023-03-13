import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

class EnergyDemandModel:
    def __init__(self):
        self.data = None
        self.model = None
        
    def load_data(self, data_path):
        self.data = pd.read_csv(data_path)
    
    def preprocess_data(self):
        # Remove unnecessary columns
        self.data.drop(['id', 'date'], axis=1, inplace=True)
        
        # Split into features and target
        X = self.data.drop('energy_demand', axis=1)
        y = self.data['energy_demand']
        
        # Scale the features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Split into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
        
        # Return the train and test sets
        return X_train, X_test, y_train, y_test
        
    def train_model(self, X_train, y_train):
        # Train a linear regression model
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)
        
    def evaluate_model(self, X_test, y_test):
        # Make predictions on the test set
        y_pred = self.model.predict(X_test)
        
        # Compute the R2 score and RMSE
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        
        # Print the results
        print(f'R2 score: {r2:.3f}')
        print(f'RMSE: {rmse:.3f}')
        
    def visualize_data(self):
        # Visualize the energy demand distribution
        sns.histplot(self.data['energy_demand'], kde=True)
        plt.show()
        
        # Visualize the correlation matrix
        corr_matrix = self.data.corr()
        sns.heatmap(corr_matrix, annot=True)
        plt.show()
