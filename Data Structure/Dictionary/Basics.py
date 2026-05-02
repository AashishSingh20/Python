# Dictionary Stores Data in Key Value Pair
# Unordered, Keys are Unique and immutable
# Keys cannot be a list,special character, set, dictionary, (any mutable datatype)

# d = {}
# print(type(d))

# d = {"name": "Aashish", "Email": "aashish002@gmail.com", "Contact": 234511}
# print(d)

# print(d["name"])

# Values can be changed but keys cannot

# d1 = {"name": "Aashish", "Email": "aashish002@gmail.com", "Contact": 234511, "name" : "Karan"}  # Latest changes will be considered
# print(d1)

# print(d.keys())
# print(d.values())

# d1 = {"course": "Mahine Learning"}
# d.update(d1)
# print(d)

# print(d.fromkeys((1,2,3),('a','b','c')))  # Also a way to create and initialize Dictionary

# ************************ Dictionary comprehension ******************* #

students = ["Arun", "Aashish", "Kunal"]
marks = ["70","95","85"]

student_marks = {}
# for student, mark in zip(students,marks):    # Zip combines students and marks
#     student_marks[student] = mark

# print(student_marks)

# OR #

student_marks = {student:marks for student, marks in zip(students,marks)}
print(student_marks)