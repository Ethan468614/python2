class Dog:
    species = "Canis familiaris"  

    def __init__(self, breed, name):
        self.breed = breed          
        self.name = name            

    def display_info(self):
        print(f"Dog Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")

dog1 = Dog("Labrador", "Buddy")
dog2 = Dog("German Shepherd", "Max")
dog1.display_info()
print()  
dog2.display_info()




        
