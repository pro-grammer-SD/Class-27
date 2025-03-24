class Vehicle(object):
    """Vehicle Class"""
    
    def __init__(self, max_speed: int, mileage: int):
        super(Vehicle, self).__init__() # my mind-chennai "super" kings
        
        self.ms = max_speed
        self.ma = mileage
         
        print("Vroom Vroom!!! - Says your instantiated vehicle!")
        
    def intro(self):
        return f"Max-Speed:\n\t{self.ma}\nMileage:\n\t{self.ms}"
            
if __name__ == "__main__":
    Vehicle_1 = Vehicle(max_speed=200, mileage=40000)
    print(Vehicle_1.intro())