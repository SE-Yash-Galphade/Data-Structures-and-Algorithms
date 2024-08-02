# Accessing/ Traversing a List

shoppingList = ['Milk', 'Cheese', 'Butter']

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + "+"
    print(shoppingList[i])

# insert:
#     insert()
#     append()
#     extend()
# update
# Can be done through indexing
# List slicing = Indexing
#    [:] = Slicing Operator

# delete


#STRINGS AND LISTS

a = 'spam'
b=list(a)
print(b)

c = 'spam spam spam'
d=c.split()
print(d)

e = 'spam-spam1-spam2'
delimiter = '-'
f = e.split(delimiter)
print(f)

g = 'spam-spam1-spam2'
delimiter1 = 'a'
h = g.split(delimiter1)
print(h)

print(delimiter1.join(h))


# Lists vs Arrays

import numpy as np

myArray = np.array([1,2,3,4,5,6])
myList = [1,2,3,4,5,6]

print(myArray/2)
# print(myList/2)         # Throws an error

myArray1 = np.array([1,2,3,4,5,6, 'a'])     # All the elements of the array are converted into strings and printed as string on the console/terminal
myList1 = [1,2,3,4,5,6, 'a']

print(myArray1)
print(myList1)