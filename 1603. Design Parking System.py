class ParkingSystem:
    parking = [0,0,0]

    def __init__(self, big: int, medium: int, small: int):
        self.parking[0] = big
        self.parking[1] = medium
        self.parking[2] = small
        

    def addCar(self, carType: int) -> bool:
        if self.parking[carType-1] > 0:
            self.parking[carType-1] -= 1
            return True
        return False
        
