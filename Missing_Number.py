# def missing_number(arr, n):
#     # Calculate the sum of first n natural numbers
#     total = n * (n + 1) // 2
    
#     # Calculate the sum of numbers in the array
#     sum_arr = sum(arr)
    
#     # Find the missing number by subtracting sum_arr from total
#     missing = total - sum_arr
    
#     return missing
 
# # Example
# print(missing_number([1, 2, 3, 4, 6], 6))  # Output: 5


# Example 1

# def missing_number(arr, n):
#     total = n * (n+1) // 2
#     sum_arr = sum(arr)
#     missing = total - sum_arr 

#     return missing

# print(missing_number([1,2,3,4,6], 6))

# Example 2

def miss(arr, n):
    total = n * (n+1) // 2
    sum_arr = sum(arr)

    missing = total - sum_arr

    return missing

print(miss([5,3,4,7,2,1,8,9], 9))