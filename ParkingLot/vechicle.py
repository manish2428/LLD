from abc import ABC, abstractclassmethod
from .EnumsType import VType


class Vehicle(ABC):
    def __init__(self, liscense_number):
        self.liscense_number = liscense_number

    @abstractclassmethod
    def get_type(self):
        pass

class Car(Vehicle):
    def __init__(self, liscense_number):
        self.liscense_number = liscense_number
        self.Vype =VType.CAR

    def get_type(self):
        return self.Vtype
    
class Bike(Vehicle):
    def __init__(self, liscense_number):
        self.liscense_number = liscense_number
        self.Vype =VType.BIKE

    def get_type(self):
        return self.Vtype
    
class Truck(Vehicle):
    def __init__(self, liscense_number):
        self.liscense_number = liscense_number
        self.Vype =VType.TRUCK

    def get_type(self):
        return self.Vtype
    

