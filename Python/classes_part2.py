# cust_name = "Karthik"
# cust_email = "karthik@gmail.com"
# age = 40
# cus_orders = []


# def add_order(order_details):
#     pass

# def calculate_total():
#     pass


# class Customer:
#     def __init__(self):
#         pass
    
#     def add_order(order_details):
#         pass

#     def calculate_total():
#         pass
    
# cust1 = Customer("Karthik", "karthik@gmail.com")
# cust2 = Customer("y", "y@gmail.com")
# cust3 = Customer("z", "z@gmail.com")
# cust4 = Customer("c", "c@gmail.com")


# -- Encapsulation

# -- Inheritence

# 1. Single Inheritance

class Animal: # parent class / base class
    def sound(self):
        return "Animal Sound"

class Dog(Animal):  # child class / derived class
    def get_name(self):
        return "This is Tommy"

# dog = Dog()
# print(dog.get_name())
# print(dog.sound())


# 2. Multiple Inheritence

class Animal: # parent class / base class
    def sound(self):
        return "Animal Sound"

class Species: # parent class
    def get_species(self):
        return "Hey, I'm a dog which lives on Earth"

class Dog(Animal, Species):  # child class / derived class
    def get_name(self):
        return "This is Tommy"

# dog = Dog()
# print(dog.get_name())
# print(dog.sound())
# print(dog.get_species())


# 3. Multi-level Inheritance

class GrandParent():
    def get_grandparent_properties(self):
        return "Owns a complex in HSR Layout"
    
class Parent(GrandParent):
    def get_parent_properties(self):
        return "Owns a mansion in Bangalore"

class Child(Parent):
    def get_child_properties(self):
        return "Owns a Bugati"

child_obj = Child()
# print(child_obj.get_grandparent_properties())

# 4. Hybrid Inheritence

class GrandParent():
    def get_grandparent_properties(self):
        return "Owns a complex in HSR Layout"
    
class Father(GrandParent):
    def get_parent_properties(self):
        return "Owns a mansion in Bangalore"
    
class Mother():
    def get_mother_properties(self):
        return "Owns lot of equity in X company" 

class Child(Father, Mother):
    def get_child_properties(self):
        return "Owns a Bugati"

child_obj = Child()
print(child_obj.get_grandparent_properties())
print(child_obj.get_mother_properties())