from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    @abstractclassmethod
    def vehicle_type():
        pass
    
    @abstractclassmethod
    def get_plate_number():
        pass

class TwoWiller(Vehicle):
    def __init__(self, plate_number):
        self.vehicle_type = 2
        self.plate_number = plate_number
        self.isEv = False

    def vehicle_type(self):
        return self.vehicle_type
    
    def get_plate_number(self):
        return self.plate_number
    
    def is_ev(self):
        return self.isEV
    
    
class FourWiller(Vehicle):
    def __init__(self, plate_number):
        self.vehicle_type = 4
        self.plate_number = plate_number
        self.isEv = False

    def vehicle_type(self):
        return self.vehicle_type
    
    def get_plate_number(self):
        return self.plate_number
    
    def is_ev(self):
        return self.isEV
    
class EVTwoWiller(Vehicle):
    def __init__(self, plate_number):
        self.vehicle_type = 2
        self.plate_number = plate_number
        self.isEv = True

    def vehicle_type(self):
        return self.vehicle_type
    
    def get_plate_number(self):
        return self.plate_number
    
    def is_ev(self):
        return self.isEV

class EVFourWiller(Vehicle):
    def __init__(self, plate_number):
        self.vehicle_type = 4
        self.plate_number = plate_number
        self.isEv = True

    def vehicle_type(self):
        return self.vehicle_type
    
    def get_plate_number(self):
        return self.plate_number
    
    def is_ev(self):
        return self.isEV
    