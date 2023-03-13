import pandas as pd
import numpy as np

class LifeCycleAssessment:
    def __init__(self, product_name):
        self.product_name = product_name
        
    def get_emissions(self):
        """
        Get the carbon emissions data for the product from a database
        """
        emissions_data = pd.read_csv("emissions_database.csv")
        product_data = emissions_data[emissions_data["Product"] == self.product_name]
        return product_data["Carbon Emissions"].values[0]
    
    def calculate_impact(self, usage_time):
        """
        Calculate the environmental impact of using the product for a certain amount of time
        """
        emissions = self.get_emissions()
        usage_in_hours = usage_time * 365 * 24
        return emissions * usage_in_hours
    
    def recommend_alternatives(self):
        """
        Recommend alternative products with lower environmental impact
        """
        emissions_data = pd.read_csv("emissions_database.csv")
        alternatives = emissions_data[emissions_data["Product"] != self.product_name]
        alternatives = alternatives.sort_values("Carbon Emissions", ascending=True)
        return alternatives.head(5)["Product"].tolist()
