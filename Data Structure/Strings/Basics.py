# # ************ ASCII Codes of characters ********************* #

# print(ord('A'))

# ***************** Unicode Representation ********************* #

# print('\u03A9')  # Prints Omega Symbol

# print('\u03A3')  # Prints Summation Symbol

# print('\u0973')  # Prints A in Hindi Symbol

# print(chr(975))

# string1 = "pwskills"
# print(type(string1))


# # ********************** Concatenation ****************** #

# string1 = "hello "
# string2 = "world"

# print(string1 + string2)
# print(string1 + ", " + string2)

# # ******************* Extract a String ****************** #

# string1 = "I'm a good Student"

# print(string1[7])
# print(string1[0:6])

# print(string1[0:])  # Gets Chracter from 0'th index till last index
# print(string1[:6]) # Gets character from 0th index till 6th index

# print(string1[0:7:2])  # Skips Every 2nd Character

# print(string1[::-1])  # Prints in Reverse from -1 index

# # ********************* Modification of String ******************** #

# s = "I am a Teacher"
# print(s)

# s = s.replace("Teacher", "Student")
# print(s)

# str = "Teacher and Student and Parent"
# str = str.replace("and", "or")
# print(str)

# text1 = "hello"
# text2 = "HELLO"

# print(text1.upper())
# print(text2.lower())

# # **************************** String Searching **************** #

# email = "aashish123@gmail.com"

# if "@" in email:
#     print("Valid Email")
# else:
#     print("Invalid Email")


# # ******************* String Comparison ********************* #

# str1 = "Hello"
# str2 = "hello"
# print(str1.lower() == str2)

# reg_username = ["DarkKnight","Hunter","Thor"]
# new_user = "Fighter"

# if new_user in reg_username:
#     print("Username already in use")
# else:
#     print("Username available")

# product_code = "A012"
# scanned_code = input("Enter the Product Code: ")

# if product_code == scanned_code:
#     print("Price is 200")
# else:
#     print("Invalid Product code")


# # ********************* String Ordering ******************* # 

# names = ["Aashish", "Kunal", "Mayur", "Karan"]
# print(sorted(names)) 

# # *********************** Common String Operations ******************** #

# input_str = "       Aashish        "
# print(input_str.strip())   # Trims Leading and Trailing whitespaces(Not remove spaces between 2 words)


# # ******************** String Spliting ******************* #
# data = "Aashish, boy,and,a,student"
# Student_Info = data.split(",")
# print(Student_Info)

# name = Student_Info[0]
# gender = Student_Info[1]

# print(gender)

# # ************************* Escape Sequence ***************** #(Special combination of charactres used in string "\n","\t")

# address = "123, Naraja, \nRaganehi, \nGundurgarh"
# print(address)

# ************************ String Formatting ****************** #(Creating a String with Placeholder for variables)

username = "Aashish"
print(f"Hello {username}, how are you?")
