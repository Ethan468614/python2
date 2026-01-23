class Vehcle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modele = Vehcle(240,34) 

print("The maximum speed of the vehicle is:", modele.max_speed)
print("The mileage of the vehicle is:", modele.mileage)