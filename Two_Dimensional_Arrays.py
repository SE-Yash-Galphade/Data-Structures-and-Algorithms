import numpy as np

#      DATA
# Day1 = 11, 15, 10, 6
# Day2 = 10, 14, 11, 5
# Day3 = 12, 17, 12, 8
# Day4 = 15, 18, 14, 9

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

print(twoDArray)

print("************INSERTION IN A 2D-ARRAY*********")

# newtwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]], axis=1)
# print(newtwoDArray)

# newtwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]], axis=0)
# print(newtwoDArray)

#Append function can also be used in case to add the new row or new column directly to the last index of the 2D array. Also it does takes array name, new values and axis as parameters.


print("************ACCESSING ELEMENTS OF A 2D-ARRAY*********")

# twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print("Error, Invalid Index Specifiers")
    else:
        print(array[rowIndex][colIndex])

accessElements(twoDArray, 1, 2)
accessElements(twoDArray, 2, 3)


print("************TRAVERSING A 2D-ARRAY*********")

def traverseTwoD(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverseTwoD(twoDArray)

print("************DELETION IN A 2D-ARRAY*********")

import numpy as np

print(twoDArray)
newTDArray = np.delete(twoDArray, 0, axis=0)
print(newTDArray)

newTDArray1 = np.delete(twoDArray, 1, axis=1)
print(newTDArray1)

