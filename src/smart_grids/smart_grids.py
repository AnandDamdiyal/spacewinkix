import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class SmartGrid:
    def __init__(self, energy_production, energy_consumption):
        self.energy_production = energy_production
        self.energy_consumption = energy_consumption
        self.energy_balance = energy_production - energy_consumption
        
    def optimize(self, energy_demand):
        energy_deficit = energy_demand - self.energy_balance
        if energy_deficit < 0:
            self.energy_balance -= energy_deficit
        else:
            self.energy_production += energy_deficit
    
    def plot(self):
        plt.plot(np.arange(len(self.energy_production)), self.energy_production, label="Energy Production")
        plt.plot(np.arange(len(self.energy_consumption)), self.energy_consumption, label="Energy Consumption")
        plt.plot(np.arange(len(self.energy_production)), self.energy_balance, label="Energy Balance")
        plt.legend()
        plt.show()
