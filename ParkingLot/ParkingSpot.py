from .ParkingLot import ParkingLot
from vechicle import Vehicle
from EnumsType import VType
class ParkingSpot():
    def __init__(self, spot_number, vehicle_type:VType.CAR):
        self.spot_number = spot_number
        self.vehicle_type = vehicle_type
        self.park_vehicle = None

    def is_available(self)->bool:
        if self.park_vehicle is None:
            return True
        return False
    
    def park_vehicle(self, vehicle: Vehicle):
        if self.park_vehicle == None:
            self.park_vehicle = vehicle
        else:
            raise ValueError("This Parking spot is already full")

    def unpark_vehicle(self):
        if self.park_vehicle != None:
            self.park_vehicle = None
        
        else:
            raise ValueError("No vehicle is Parked here!!")
        

    def get_parked_vehicle(self, vehicle:Vehicle):
        return self.park_vehicle

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_spot_number(self):
        return self.spot_number



    




        