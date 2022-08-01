class ParkingSystem:
    
    big = 0
    mid = 0
    sml = 0
    
    def __init__(self, big: int, medium: int, small: int):
        
        self.big = big
        self.mid = medium
        self.sml = small
        
    def addCar(self, carType: int) -> bool:
        
        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True
            else:
                return False
            
        if carType == 2:
            if self.mid > 0:
                self.mid -= 1
                return True
            else:
                return False
            
        if carType == 3:
            if self.sml > 0:
                self.sml -= 1
                return True
            else:
                return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)