"""
A 3D list in Python is a list of lists of lists. It can be visualized as a cube or a collection of 2D matrices stacked together. Each element in a 3D list is accessed using three indices:
"""
# First index → Represents the depth (which 2D matrix you're in).
# Second index → Represents the row in that matrix.
# Third index → Represents the column in that row.

# 3D list (2 matrices, 3 rows, 4 columns)

three_d_list = [
    [  
        #First matrix[0]
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    #Second matrix[1]
    [  
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]
]

# Accessing an element
# print(three_d_list[1][0][3]) #16  

for matrix in three_d_list:
    for row in matrix:
        for elements in row:
            print(elements) 
print() #New line

# Task 1: Create a 3D List
"""
# Write a Python program that initializes a 3D list with random numbers between 1 and 100. The list should have the following structure:

# 3 matrices (depth)
# 4 rows per matrix
# 5 columns per row
"""
#Task 2: Access and Modify Elements and Iterate those elements
"""
Access and print the element in the 2nd matrix, 3rd row, and 4th column.
Modify the value in the 1st matrix, 2nd row, and 5th column to 999.
Print the entire updated 3D list.
"""

