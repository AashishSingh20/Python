# Lists are ordered Collections of items 
# Lists are Mutable(Can be changed)
# Can Store Everything like a shopping bag

# print(type([]))

# grocery_list = ["Milk", "Mango", 1, 6, True, 2+5j, 5.4]
# print(grocery_list)

# grocery_list[1] =  "Banana"
# print(grocery_list)

# # ************* Append ************** #(Add Elements to the end of the list)

# list1 = ["Mango","Banana"]
# print(list1)

# list1.append("Guava")
# print(list1)


# # ***************** Insert *************** #

# bus_seat = ["Raj", "Aashish", "Kunal", "Soham", "Lakshman"]
# print(bus_seat)
# bus_seat.insert(0,"Darshan")
# print(bus_seat)

# # **************** Extend ************** #

# my_list = ["Mango", "Banana", "Guava"]
# brothers_list = ["Potato", "Spinach", "Coriander"]

# my_list.extend(brothers_list)
# print(my_list)

# # ******************* Concatenate **************** #
# print(my_list + brothers_list)

# ************************ Repeatation *************************** #

# print("*" * 10)
# print([1,2] * 5) 

# # ****************** Deep Copy & Shallow Copy ******************* #

# grocery_list = ["Banana", "Milk", "Potato", "Turmeric"]
# a = grocery_list    # Shallow Copy(Change with change in other list)
# b = grocery_list.copy()   # Deep Copy(Doesn't change with change in other list)

# # ******************* Sorting List ****************** #

# book_list = ["Machine Learning", "AI", "Web Dev", "DSA"]
# print(sorted(book_list))


# ********************* List Comprehension *********************** #

# prices = [10,20,30,40,50]
# doubled_price = []
# for i in prices:
#     doubled_price.append(i*2)
# print(doubled_price)

# doubled_price2 = [price * 2 for price in prices]  # Same as Above, but Faster
# print(doubled_price2)

# names = ["aashish", "karan", "Rohit"]
# print([name.capitalize() for name in names])

# file_name = ["abc.pdf", "123.jpg", "test.py", "file2.docx", "photo.png"]
# print([file.split(".")[-1] for file in file_name])

# # ************************ Conditional List Comprehension ********************** #

# email_address = ["aashish123@gmail.com", "raghav345@hotmail.com", "sun1330@yahoo.com", "kunal33t@gmail.com"]

# print([email for email in email_address if email.endswith("@gmail.com")])

# *************************** Nested List Comprehension ************************* #

pairs = []

# for x in [1,2,3]:   # Normal Nested Loop 
#     for y in [4,5,6]:
#         pairs.append([x,y])

# print(pairs)

# pairs = [[x,y] for x in [1,2,3] for y in [4,5,6]]
# print(pairs)

# *************************** List as Stack an queue ********************* #
# ************* Stack ************* #

# stack_of_plates = []
# stack_of_plates.append("Plate1")
# stack_of_plates.append("Plate2")
# stack_of_plates.append("Plate3")
# stack_of_plates.append("Plate4")

# print(stack_of_plates)

# stack_of_plates.pop()
# print(stack_of_plates)

# ************* Queue ************* #

# from collections import deque

# checkout = deque()

# checkout.append("Customer1")
# checkout.append("Customer2")
# checkout.append("Customer3")
# checkout.append("Customer4")

# print(checkout)

# while checkout:
#     customer = checkout.popleft()
#     print("Serving", customer)

from queue import Queue

print_queue = Queue()

print_queue.put("Job1")
print_queue.put("Job2")
print_queue.put("Job3")


while not print_queue.empty():
    print_job = print_queue.get()
    print(print_job)