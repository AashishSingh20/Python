# *********************** Inbuilt Functions ************************** #(len, print, type, etc)
# print("Hello")
# print(len("hello"))

# **************** User Defined Functions ******************** #

# def greet(n):     # n is an argument
#     return (f"Hello {n}")

# print(greet("Aashish"))

# print(greet("Ankur") + " How are you?")  # Concatenation only eorks with when function has return statements


# **** Write Function that take list as input and return all numeric values **** #

# def only_numeric(a):
#     n = []
#     for i in a:
#         if type(i) == int or type(i) == float:
#             n.append(i)
#     return n

# numeric = only_numeric([1,3,4,6,"Aashish","Raj","False",2.6,5.1])
# print(numeric)

# ****************** Variable Length Argument ********************* #
# args and kwargs are not python keywords instead of it we can use any word

# def sum(*args):
#     s = 0
#     for i in args:
#         s = s+i
#     return s

# print(sum(2,6,8))

# def test1(*args):
#     return args

# print(test1("Hello", 1, 3, 5, True, 2.4, 6.5, [1,2,3], (5,6,7)))


# # Creating a Function that should accept any no of arguments and treat it as key value pair

# def kwarg_fun(**kwargs):
#     return kwargs

# print(kwarg_fun(a = 2, b = 6, c = [1,2,3,4], d = (4,5,6,7)))

# # *************************** Python Namespace ************************* #

# new_message = "Welcome"    # new_message = Global Variable 
# def greet():
#     message = "Hello"   # message = Local Variable
#     print(message)

# greet()
# print(new_message)


# ************************** Function Inside Function ************************* #
# Calling From Inside
def marks_in_subjects(**kwargs):
    def total_marks(marks_list):
        return sum(marks_list)
    marks_list = []
    for subject, marks in kwargs.items():
        marks_list.append(marks)
    return total_marks(marks_list)

print(marks_in_subjects(a = 15, b = 45, c = 72))

# Calling from Outside
def total_marks(marks_list):
    return sum(marks_list)

def marks_in_subjects(**kwargs):
    marks_list = []
    for subject, marks in kwargs.items():
        marks_list.append(marks)
    return total_marks(marks_list)

print(marks_in_subjects(a = 15, b = 45, c = 72))
