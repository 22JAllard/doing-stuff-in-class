class Car:
    def __init__(self, registration, make):
        self.registration = registration
        self.make = make
        self.mileage = 0
        self.dateofinspection = None

    def getinfo(self):
        return self.registration, self.make, self.mileage, self.dateofinspection
    
    def set_inspection(self, dateofinspection):
        self.dateofinspection = dateofinspection

new_car = Car("120984912", "Aiasfhigia")
print(new_car.getinfo())
new_car.set_inspection("1047125781578")
print(new_car.getinfo())

    