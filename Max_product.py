

# myarray = [1,7,3,4,9,5]


# def max_product(arr):
#     # for i in myarray:
#     #     if myarray[i] > myarray[i+1]:
#     #         num1 = myarray[i]
#     num1 = 0
#     num2 = 0

#     num1 = max(myarray)
#     print(num1)

#     for i in range(len(myarray)):
#         if myarray[i] < num1 and myarray[i] > myarray[i-1]:
#             num2 = myarray[i]
    
#     print(num2)


# max_product(myarray)


def max_product(arr):
    max1, max2 = 0, 0
 
    for num in arr:  
        if num > max1: 
            max2 = max1 
            max1 = num  
        elif num > max2:  
            max2 = num  

    return max1 * max2  
 
arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr))  
