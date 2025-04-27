from abc import ABC,abstractmethod 

class Vehicle:

    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car is starting")

    def stop_engine(self):
        print("Turning off my Car")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike is starting")

    def stop_engine(self):
        print("Turning off my Bike")
        
def drive(vehicle : Vehicle):
    vehicle.start_engine()
    print("-----------------RUNNING-----------------")
    vehicle.stop_engine()

drive(Bike())
drive(Car())


'''
Abstraction means showing only the essential details while hiding the unnecessary complexity.
It's like using an interface or an abstract class to define what something can do, not how.


-Simplifies usage
-Encourages consistent behavior via contracts (e.g., interfaces)

'''