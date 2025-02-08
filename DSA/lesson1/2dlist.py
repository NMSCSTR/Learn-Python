# Topic for Discussion: 2D Lists in Python

"""
Overview:
A 2D list in Python is essentially a list of lists, where each individual list can hold multiple items. It is useful for representing data in a tabular or matrix-like structure. It’s a natural way of dealing with problems where data is organized in rows and columns, such as a matrix or a grid.
"""

# Key Points for Discussion:
# Definition of 2D List:
"""
A 2D list is a list that contains other lists as its elements.
Think of it as a matrix or grid with rows and columns.
"""
# Example: A 2D list representing a matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]].

"""
Properties of 2D Lists:

Nested Structure: Each element of the main list is itself a list (sublist).
Indexing: 2D lists are accessed by two indices—one for the row and one for the column. The first index is for the row (starting from 0), and the second index is for the column (also starting from 0).
Mutable: The elements of a 2D list can be changed, just like 1D lists.


2D List Representation:

Rows and Columns: The rows are the outer lists, and the columns are the elements within each inner list.
Shape of a 2D List: The shape is represented by the number of rows and the number of columns. For example, a list with 3 rows and 4 columns is a 3x4 matrix.

"""

# Creating a 2D List:
# A 2D list can be created in several ways, such as initializing it manually with nested lists, using loops, or using list comprehensions.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Indexing and Accessing Elements in 2D Lists:
# Access elements using two indices: matrix[row][column].
print(matrix[1][2])

# Traversing a 2D List:
# Use nested loops (or list comprehensions) to traverse through all the elements in a 2D list.
# Example: A nested loop can be used to access each element in a row and print it.
for num in matrix:
    for n in num:
        print(n)


# Manipulating Elements in 2D Lists:
"""Modify an element using its indices: matrix[row][column] = new_value.
You can also add rows or columns by appending or inserting lists.
Example: matrix.append([10, 11, 12]) adds a new row to the matrix.
"""
# Applications of 2D Lists:

# Representing matrices in mathematics.
# Storing tabular data such as spreadsheets or databases.
# Grids or maps for games (like chessboards, tic-tac-toe boards).
# Image data representation (pixel values in an image).
# Performance Considerations:

# 2D lists can grow in complexity, and accessing elements might take more time compared to simple 1D lists, especially if the matrix is large.
# When using large 2D lists (e.g., for matrices or images), consider more efficient structures such as NumPy arrays for better performance.