print("######### CREATING AN ARRAY ########\n")

import array

my_array = array.array('i')

my_array1 = array.array('i', [1,2,3,4])
print(my_array1)

import numpy as np
np_array = np.array([], dtype=int)

np_array1 = np.array([1,2,3,4])
print(np_array1)


print("########### INSERTING INTO AN ARRAY ##########\n")

import array
array_2 = array.array('i', [1,2,3,4])
array_2.insert(0, 5)  # (Index, Value)
print(array_2)

array_2.insert(2, 6)  
print(array_2)

print("########## TRAVERSING IN AN ARRAY ###########\n")

arr2 = array.array('i', [1,2,3,4,5,6])
arr3 = array.array('d', [1.12, 2.23, 4.78, 8.90])

def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr2)
traverseArray(arr3)


print("########## ACCESSING AN ELEMENT OF AN ARRAY ###########\n")

from array import * 

arr4 = array('i', [1,2,3,4,5,6])

def accessElement(array, index):
    if index >= len(array):
        print("There is not any element in this index")
    else:
        print(array[index])

accessElement(arr4, 3)
accessElement(arr4, 8)

