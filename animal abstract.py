from abc import ABC, abstractmethod

class Animal(ABC):

    def move(self):
        pass

class human(Animal):
    def move(self):
        print("I can walk and run")

class snake(Animal):
    def move(self):
        print("I can crawl")

class Dog(Animal):    
    def move(self):
        print("I can bark ")

class lion(Animal):
    def move(self):
        print("I can roar")

R = human()
R.move()

K = snake()
K.move()

R = Dog()
R.move()

K = lion()
K.move()