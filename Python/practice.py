# 2 * 1 = 2
# 2 * 2 = 4

# 2 * 10 = 20

# num = int(input("Enter table to print: "))

# for i in range(1, 11):
#     print(f"{num} * {i} = {num*i}")
    

for i in range(2, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i*j}")
    print("-----------------------")