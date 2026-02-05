class BMW:
    def clour(self):
        print("BMW looks good in black")

    def model(self):
        print("BMW M5 is a popular model")    

    def type(self):
        print("BMW is a luxury car")

class Ferrari:
    def clour(self):
        print("Ferrari looks good in red")

    def model(self):
        print("Ferrari F8 is a popular model")    

    def type(self):
        print("Ferrari is a sports car")


car1 = BMW()
car2 = Ferrari()
for car in (car1, car2):
    car.clour()
    car.model()
    car.type()
    
                        