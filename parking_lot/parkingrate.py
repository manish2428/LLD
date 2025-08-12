class ParkingRate:
    MINUTE = 0.5
    HOURLY = 20
    DAY = 200

    def get_minute_charge():
        return ParkingRate.MINUTE
    
    def get_hourly_charge():
        return ParkingRate.HOURLY

    def get_daily_charge():
        return ParkingRate.DAY


