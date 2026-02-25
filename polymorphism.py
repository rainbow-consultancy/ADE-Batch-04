
# poliy-morphism

# 1. Duck Typing
# 2. method overriding
# 3. method overloading -- not supported in python


class Dog:
    def sound(self):
        return "Sound of the Dog"

class Cat:
    def sound(self):
        return "Sound of Cat"

class Cow:
    def sound(self):
        return "Sound of the Cow"
    

def animal_sound(animal):
    print(animal.sound())
    

# animal_sound(Dog())
# animal_sound(Cat())
# animal_sound(Cow())


class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Sound of the Dog")

class Cat(Animal):
    def sound(self):
        print("Sound of Cat")
        
a = Animal()
b = Dog()
c = Cat()

# a.sound(1)
# b.sound()
# c.sound()


class Animal:  # parent class
    def __init__(self, name):
        self.name = name
        print("Animal constructor called")

class Dog(Animal): # child class
    def __init__(self, name):
        super().__init__(name)
        print("Dog constructor called")

d = Dog("Rocky")
print(d.name)
                
# *args *kwargs

# git changes

