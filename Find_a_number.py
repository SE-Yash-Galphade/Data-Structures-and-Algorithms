import numpy as np

myArray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print("Number is Present")
        # else:
        #     print("The Number is not present")

linear_search(myArray, 7)

