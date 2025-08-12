from abc import ABC, abstractmethod
from .enum import VechicleType

class Vehicle(ABC):
    @abstractmethod
    def get_number_plate(self):
        pass
    @abstractmethod
    def get_vehicle_type(self):
        pass

    @abstractmethod    
    def is_assigned(self):
        pass

class Bus(Vehicle):
    def __init__(self, number_plate):
        self.number_plate = number_plate
        self.vehicle_type = VechicleType.Bus
        self.spot_assigned = False

    def get_number_plate(self):
        return self.number_plate
    
    def get_vehicle_type(self):
        return self.vehicle_type
    
    def is_assigned(self):
        return self.spot_assigned
    

class Truck(Vehicle):
    def __init__(self, number_plate):
        self.number_plate = number_plate
        self.vehicle_type = VechicleType.Trck
        self.spot_assigned = False

    def get_number_plate(self):
        return self.number_plate
    
    def get_vehicle_type(self):
        return self.vehicle_type
    
    def is_assigned(self):
        return self.spot_assigned
    

class Car(Vehicle):
    def __init__(self, number_plate):
        self.number_plate = number_plate
        self.vehicle_type = VechicleType.Car
        self.spot_assigned = False

    def get_number_plate(self):
        return self.number_plate
    
    def get_vehicle_type(self):
        return self.vehicle_type
    
    def is_assigned(self):
        return self.spot_assigned
    


class TwoWheeler(Vehicle):
    def __init__(self, number_plate):
        self.number_plate = number_plate
        self.vehicle_type = VechicleType.Bike
        self.spot_assigned = False

    def get_number_plate(self):
        return self.number_plate
    
    def get_vehicle_type(self):
        return self.vehicle_type
    
    def is_assigned(self):
        return self.spot_assigned
    


class SUV(Vehicle):
    def __init__(self, number_plate):
        self.number_plate = number_plate
        self.vehicle_type = VechicleType.SUV
        self.spot_assigned = False

    def get_number_plate(self):
        return self.number_plate
    
    def get_vehicle_type(self):
        return self.vehicle_type
    
    def is_assigned(self):
        return self.spot_assigned
    

    

