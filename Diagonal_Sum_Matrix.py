def diagonal_sum(matrix):
    # Initialize the sum to 0
    sum = 0
 
    # Iterate through the rows of the matrix
    for i in range(len(matrix)):
        # Add the diagonal element to the total sum
        sum += matrix[i][i]
 
    return sum

myList2D= [[1,2,3], [4,5,6], [7,8,9]]
print(diagonal_sum(myList2D)) # Output: 15
