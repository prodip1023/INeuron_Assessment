"""Write an efficient algorithm that searches for a value target in an m x n integer matrix. This matrix has the following properties:

Integers in each row are sorted from right to left.

The first integer of each row is greater than the last integer of the previous row.

                              Example-: 

                                        Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3

                                         Output: True"""

def searchMatrix(matrix,target):
    if not matrix: return False
    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    # Start from the top-right corner of the matrix
    row, col = 0, num_cols - 1
    while row < num_rows and col >= 0:
        # If the current element is equal to the target, return True
        if matrix[row][col] == target:
            return True
        # If the current element is larger than the target, move left (go up a column)
        elif matrix[row][col] > target:
            col -= 1
        # Otherwise, move down (go down a row)
        else:
            row += 1
# If we've reached the end of the matrix without finding the target, return False
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
final = searchMatrix(matrix=matrix,target=target)
print("Final Answer:",final)




            


    

