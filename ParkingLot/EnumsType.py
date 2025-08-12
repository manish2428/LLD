from enum import Enum

class VType(Enum):
    CAR = 1
    TRUCK = 2
    BIKE = 3

class PaymentStatus(Enum):
    PROCESSING = 1
    COMPLETED = 2
    FAILED = 3

class SpotType(Enum):
    COMPACT = "Compact"
    LARGE = "Large"
    BIKE = "Bike"