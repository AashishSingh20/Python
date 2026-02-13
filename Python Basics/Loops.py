'''
# While Loop
num = int(input("Enter value of n: "))
i = 1
while(i<=num):
    print(i)
    i += 1
else:
    print("Loop executed successfully!")
'''

'''
# For Loop
a = "aashish"
for char in a:
    print(char)


l = [1,55,"aashish","fast"]
for list in l:
    print(list)
'''

'''
# range
print(list(range(0,10)))  # Gives us a list of numbers ranging from 0 to 10 except 10

for i in range(10):
    print(i) 

# syntax range(start,stop,step)
print(list(range(0,10,2)))   # print list of numbers from 0 to 9 and move 2 steps at a time

print(list(range(10)))  # automatically move from 0 to 9
'''

'''
# Printing Right angled Triangle using while loop
height = int(input("Enter Height of Triangle: "))
i = 1
while (i <= height):
    j = 1
    while (j <= i):
        print('*',end = " ")  # star marne ke baad next line par mat chale jana check ki loop khatam toh nahi hua 
        j += 1
    print()
    i += 1
'''

'''
# Printing Right angled Triangle using for loop
height = int(input("Enter Height of Triangle: "))
for i in range(height):
    for j in range(i+1): 
        print("*",end = " ")
        j += 1
    print()
    i += 1
'''

'''
number = [1,2,3,4,5,6,7]
for number in number:
    if(number == 3)  or (number == 7):  # if the number is 3 or 7 then it skips it
        continue
    print(number, end=" ")
'''

# Print only even Numbers
for i in range(11):
    if(i%2 != 0):
        print(i , end = " ")
    else:
        continue
