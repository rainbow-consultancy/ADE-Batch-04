# 1. for loop
# 2. while loop

# range(start, end, step)  -->


# for i in range(1, 11, 2):
#     print(i)
    
# for i in range(11):
#     print(i)


# x = 1

# while x <= 10:
#     print(x)
    # x = x+1
    # x+=1
    
    
# iterable items -- > strings, lists, tuple, dict, set

# for i in "Ganga":
#     print(i)
    
li = [1, 2, 3, 4, 5]

# for i in range(len(li)):
#     print(li[i])

student = {"id": 100, "name": "Lokesh", "Grade": 5}

for k, v in student.items():
    print(k, v)
    
for k in student.keys():
    print(k)
    
for k in student.values():
    print(k)