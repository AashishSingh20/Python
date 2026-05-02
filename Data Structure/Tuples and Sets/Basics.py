# Tuples are ordered collection of elements, heterogenous 
# # Tuples are immutable

# t = ()
# print(type(t))

# tuple1 = ("aashish", 4+6j, True, 1, 3, 5, 1, 4.7)
# print(tuple1)

# print(tuple1.count(1))  # Checks count of 1 

# for i in tuple1:
#     print(i,type(i))

# Rest all operations same as String and lists

# ********************** Sets ************************ #(Unique and unordered elements)

# s = {}
# print(type(s))

# set = {1,2,3,4,1,1,1,3,3,2, "aashish", "raj", "aashish", "Aashish"}
# print(set)

# set1 = {1,2,4,9,1,2,[1,2,3]}  # We Cannot put list in set as lists are mutable
# set2 = {1,3,2,1,4,4,(1,2,3)}  # Valid as tuples are immutable

# # Cannot access elements directly in sets as it is stored using hash values but we can access them using loops
# # for i in set2:
# #     print(i)

# # ***************** Remove ****************** #
# set2.remove(3)  # Will throw an error if given element is not in set

# # **************** Discard ******************* #
# set2.discard(5)  # Will not throw an error if element is not present in set
# print(set2)

# *********************** Set Operations *********************** #
# Union
# Intersection
# Difference
# Symmetric Difference

# s1 = {1,2,3,4,5}
# s2 = {3,2,6,8,1}

# print(s1.union(s2))   # Or s1 | s2
# print(s1.intersection(s2))  # Or s1 & s2
# print(s1.difference(s2))   # Or s1 - s2
# print(s1.symmetric_difference(s2))   # or s1 ^ s2

# **************** Frozen Sets ***************** #(Immutable Version of Set)

# Normal Set(We can add anytime)
s = {4,5,6,7,8}
s.add(123)
print(s)


frozen_set = frozenset([1,2,3,3,4,4,5])
print(frozen_set)
print(type(frozen_set))
# Now we cannot add or delete any elements