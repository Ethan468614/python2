class Parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age

m = Parrot("Billy", 7) 
m2 = Parrot("Max", 5)

print("{} is {} years old".format(m.name, m.age))
print("{} is {} years old".format(m2.name, m2.age))