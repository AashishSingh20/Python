# Tuples are immutable

point = (2,3)
print(point)
print(type(point))

a = ("Aashish", 2, 6, 10, True)
print(a)

name = ("Aashish", "Raj", "Ankur", "Sunil")
print(name[2])

# name[1] = "Karan"  will not work de to immutable property

box1 = ("a","b")
box2 = ("c","d")
chocolate_bag = (box1,box2)
print(chocolate_bag)

# Prints all elemtns in tuple 1 by one
for bag in chocolate_bag:
    for choc in bag:
        print(choc)