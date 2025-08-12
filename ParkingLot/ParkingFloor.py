from ParkingSpot import ParkingSpot
from typing import List
from vechicle import Vehicle
class ParkingFloor():
    def __init__(self, floor_no, spot,):
        self.floor_number = floor_no
        self.parking_spot: List[ParkingFloor] = [ParkingSpot(i) for i in range(spot)]
    
    def park_vehicle(self, vehicle:Vehicle)->bool:
        for spot in self.parking_spot:
            if spot.is_available() and spot.get_vehicle_type() == vehicle.get_type():
                spot.park_vehicle(vehicle)
                return True
        

    def unpark_vehicle(self, vehicle:Vehicle)->bool:
        for spot in self.parking_spot:
            if not spot.is_available() and spot.get_parked_vehicle() == vehicle:
                spot.unpark_vehicle()

    def display_availability(self):
        for spot in self.parking_spot:
            if spot.is_available():
                print(f"{spot.get_spot_number()} is Free!!")



    
    

