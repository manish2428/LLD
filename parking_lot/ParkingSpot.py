from abc import ABC, abstractmethod
from .enum import ParkingSpotType

class ParkingSpot(ABC):
    def __init__(self, id):
        self.id = id
        self.free = False

    @abstractmethod    
    def is_free(self):
        pass
    
    @abstractmethod
    def get_id(self):
        pass
    

#Lets assume both bus and truck lies in LargeSpot
class LargeSpot(ParkingSpot):
    def __init__(self, id):
        self.id = id
        self.free = False
        self.spot_type = ParkingSpotType.Trck

    def is_free(self):
        return self.free
    
    def get_id(self):
        return self.id
    
    def get_parking_spot_type(self):
        return self.spot_type

class TwoWeelerSpot(ParkingSpot):
    def __init__(self, id):
        self.id = id
        self.free = False
        self.spot_type = ParkingSpotType.Bike

    def is_free(self):
        return self.free
    
    def get_id(self):
        return self.id
    
    def get_parking_spot_type(self):
        return self.spot_type
    
class CompactSpot(ParkingSpot):
    def __init__(self, id):
        self.id = id
        self.free = False
        self.spot_type = ParkingSpotType.Car

    def is_free(self):
        return self.free
    
    def get_id(self):
        return self.id
    
    def get_parking_spot_type(self):
        return self.spot_type
    
class SUVSpot(ParkingSpot):
    def __init__(self, id):
        self.id = id
        self.free = False
        self.spot_type = ParkingSpotType.SUV

    def is_free(self):
        return self.free
    
    def get_id(self):
        return self.id
    
    def get_parking_spot_type(self):
        return self.spot_type
    
    
    


