import math

class CarbonCaptureAndStorage:
    def __init__(self, capture_rate, storage_capacity):
        self.capture_rate = capture_rate # metric tons per year
        self.storage_capacity = storage_capacity # metric tons
        
        self.current_captured = 0 # metric tons
        
    def capture(self, emissions):
        captured = emissions * self.capture_rate
        
        # check if the storage is not full
        if self.current_captured + captured > self.storage_capacity:
            overflow = (self.current_captured + captured) - self.storage_capacity
            captured -= overflow
        
        self.current_captured += captured
        return captured
    
    def release(self, amount):
        # check if enough carbon has been stored to release
        if amount <= self.current_captured:
            self.current_captured -= amount
            return amount
        else:
            return None
        
    def storage_utilization(self):
        return self.current_captured / self.storage_capacity * 100.0
    
    def time_to_fill(self, emissions):
        return math.ceil((self.storage_capacity - self.current_captured) / (emissions * self.capture_rate))
