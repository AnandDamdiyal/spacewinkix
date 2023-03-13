import requests
import pandas as pd

class LifeCycleAssessmentDataCollector:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openlca.org/v1/"
        
    def collect_lca_data(self, product_name):
        """
        Collects life cycle assessment (LCA) data for a specific product
        """
        # Set parameters
        endpoint = "search"
        params = {
            "apikey": self.api_key,
            "q": product_name,
            "type": "product"
        }
        
        # Make API request
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        
        # Check for errors
        if response.status_code != 200:
            raise ValueError(f"Error: {response.status_code}")
        
        # Get product ID from response
        results = response.json()
        if len(results) == 0:
            raise ValueError(f"No product found with name {product_name}")
        product_id = results[0]["id"]
        
        # Set parameters for LCA calculation
        endpoint = "calculations"
        data = {
            "functional-unit": {"amount": 1, "referenceUnit": "kg"},
            "product-system": {"id": product_id},
            "calculation-settings": {
                "detailed-calculation": True,
                "output-format": "JSON",
                "impact-method": {
                    "category": "climate change",
                    "method": "ReCiPe Endpoint (H,A)"
                }
            }
        }
        headers = {
            "Content-Type": "application/json"
        }
        
        # Make API request
        response = requests.post(f"{self.base_url}{endpoint}", json=data, headers=headers)
        
        # Check for errors
        if response.status_code != 201:
            raise ValueError(f"Error: {response.status_code}")
        
        # Convert response to pandas dataframe
        lca_df = pd.read_json(response.text, orient="columns")
        
        return lca_df
