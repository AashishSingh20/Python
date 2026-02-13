#List Stores Heterogenous type of Data  
# List are mutable

num = [1,2,3,4,5]
print(type(num))

print(num[0])  # Prints 1st element in the list
print(num[1])

lis = [1,"aashish",True,(2+4j)]
print(lis[1])   
print(lis[2])   

lis.append("Rohan")
lis.remove("Rohan")
print(lis)

lis2 = [[1,2,3],[4,5,6],[7,8,9]]
print(lis2[0])     # prints list at 0 index
print(lis2[1][2])  # Gets us element at 2nd position in 1 index list