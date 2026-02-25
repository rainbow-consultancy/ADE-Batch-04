class FirstClass:
    class_name = "This is my first class"
    
    def test_func(self):
        return "This is a test function inside class"
    

my_first_class = FirstClass()
print(my_first_class.class_name)
print(my_first_class.test_func())

# constructer

class Animal:
    # constructer method
    def __init__(self, name: str):
        self.name = name
        print("Hey, this is a constructer method")
    
    def get_name(self):
        return f"The name of the Dog is {self.name}"

my_dog = Animal("Tommy")
print(my_dog.get_name())  

my_dog2 = Animal("Puppy")
print(my_dog2.get_name())         

test = Animal("Kripton")


# Scope of the variables
class Animal:
    
    name = "Tommy"
    global my_var 
    my_var = "This is a Global variable"
    __my_private_var = "This is a private variable" # private variable
    
    # constructer method
    def __init__(self):
        print("Hey, this is a constructer method")
    
    def get_name(self):
        return f"The name of the Dog is {self.name}"
    
    def get_the_private(self):
        return f"private variable - {self.__my_private_var}"
    
    def __my_private_func(self): # private method
        return "This is a private function"
    
    def get_private_func(self):
        return self.__my_private_func()
    
    
my_obj = Animal()
print(my_obj.name)
print(my_obj.get_name())
print(my_obj.get_the_private())
# print(my_obj.__my_private_func())
print(my_obj.get_private_func())


# 1. global
# 2. Public
# 3. private
