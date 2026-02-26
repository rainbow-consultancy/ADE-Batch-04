num = int(input("Enter a Number: "))

# if isinstance(num, str) :
#     print("Warning: Please enter a valid number")
# elif int(num) < 0:
#     print(num, "is a negative number")
# elif int(num)%2 == 0:
#     print(num, "is an even number")
# else:
#     print(num, "is an odd number")

# x = 10
# print(isinstance(x, int))  # Output: True
# print(isinstance(x, str))  # Output: False

result = "It's a even number" if (num%2 == 0) else "It's a odd number"
print(result)


