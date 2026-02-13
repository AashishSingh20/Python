# Data is Stored in Key value Pair
# Keys are unique and immutable

# Prints Type of Dict
my_dict = {}
print(type(my_dict))

# Prints whole Dict
phoneBook = {"Dad": 1234, "Mom": 5678}
print(phoneBook)

# Prints value stored in Key "Dad"
print(phoneBook["Dad"])

# When repeating keys it will capture the last copy of any key
phoneBook = {"Dad": 1234, "Mom": 5678, "Dad": 456}
print(phoneBook)

# To get all Keys
print(phoneBook.keys())

# To get all values
print(phoneBook.values())

# To make changes in values
phoneBook["Mom"] = "Num Changed"
print(phoneBook)