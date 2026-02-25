# Str, int, float, bool

# python -

# list, tuple, set and dictionary (dict)

# 1. list

# v = "gshdghs"

# my_list = ["apple", "mango", "banana", 12, True, [1, 2, 4]]
# my_list.append("Kiwi")
# print(my_list)

# my_list[0] = "Orange"
# print(my_list)

# my_list.pop() 
# print(my_list)

# my_list.remove("mango")
# print(my_list)

# print(my_list.index("banana"))
# print(my_list[-1])

# mutable --
# immutable --


# 2. tuple

my_tuple = ("apple", "apple", 200, True, [1, 2], "apple", ("orange", "mango"))
# print(my_tuple[-1])

# print(my_tuple.count("apple"))
# print(my_tuple.index(200))


# 3. set

# my_set = {"apple", "apple", 200, True, "apple"}
# print(my_set)

# my_set.add("Banana")
# print(my_set)

myset_1 = {1, 2, 4, 5, 3}
myset_2 = {2, 4, 5, 7, 8}

# print(myset_1.intersection(myset_2))
# print(myset_1.difference(myset_2))


# 4. dict

my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(my_dict)

print(my_dict["key2"])
print(my_dict.get("key3"))

# add
my_dict["key4"] = "value4"
print(my_dict)

my_dict["key1"] = "Value  1 is modified"
print(my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())









