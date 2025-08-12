import time
from .enum import PaymentStatus
from .parkingrate import ParkingRate

class Ticket:
    def __init__(self, vehicle_type):
        self.entry_time = time.monotonic()
        self.exit_time = None
        self.status = PaymentStatus.Pending
        self.vehicle_type  = vehicle_type
    
    def calculate_amount(self):
        current_time = time.monotonic()
        time_diff = current_time - self.entry_time

        if time_diff > 60 and time_diff <= 60*24:
            return time_diff/60*ParkingRate.HOURLY
        elif time_diff < 60:
            return time_diff*ParkingRate.MINUTE
        else:
            return (time_diff/60)/24*ParkingRate.DAY

    def get_status(self):
        return self.status
    
    def generate_entry_ticket(self):
        print(f"Entry Time: {self.entry_time}")
        



