# data = [
#     (100, 'Lokesh', 40000),
#     (101, 'Srinath', 25000),
#     (102, 'Gagan', 50000) 
# ]

# sorted_data = sorted(data, key=lambda x: x[2])
# print(sorted_data)

# words = ["apple", "orange", "banana", "mango", "umbrella", "Airport", "Omega", "ELEPHANT"]
# word_cnt = len(list(filter(lambda w: w[0].lower() in "aeiou", words)))
# print(word_cnt)

# 1. Minimum 8 characters should be there
# 2. it should contain atleast 1 digit
# 3. it should contain atleast 1 uppercase character

def valid_password(pwd):
    if len(pwd) < 8:
        return False
    
    has_digit = any(c.isdigit() for c in pwd)
    has_upper = any(c.isupper() for c in pwd)
    
    return has_digit and has_upper

print(valid_password("qerty"))  # invalid
print(valid_password("Qerty@123"))  # valid 
print(valid_password("qerty@123")) # invalid
    



