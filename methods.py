# functions/methods in python

# static method
# def add_numbers():
#     return 10 + 20

# print(add_numbers())


# def add_numbers(a, b):
#     return a + b

# print(add_numbers(30, 30))


# def add_numbers(a, b=50):
#     return a + b

# print(add_numbers(30, 10))


# def add_numbers(a=20, b=50):
#     return a + b

# result = add_numbers(30, 10)
# print(result)


# def add_numbers(a=20, b=50):
#     print(a + b)
    
# add_numbers()


# args, kwargs

def my_fruits(*fruits):
    for fruit in fruits:
        print(fruit)

# my_fruits("Grapes", "Mangos", "Banana", "Litchi")
# print("\n2nd func result")
# my_fruits("Orange", "Apple")

def my_employees(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# my_employees(name="Karthik", age=30, country="India")  

# def is_even(num: int) -> bool:
#     return num%2 == 0

# print(is_even(20))
# print(is_even(23))

# lambda functions | anonymous functions

is_even = lambda num: num%2 == 0
# print(is_even(11))
# print(is_even(14))

# filter and map

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_nums = list(filter(lambda num: num%2 == 0, nums))
# print(even_nums)

# even_nums = list(map(lambda num: num%2 == 0, nums))
# print(even_nums)


# # map
# squared_nums = list(map(lambda num: num**2, nums))
# print(squared_nums)


def outer_function(text):
    def inner_function():
        a = 100
        print(text)
    inner_function()

outer_function("Hello Everyone, Good Morning!")