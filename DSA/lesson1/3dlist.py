# 3D list (2 matrices, 3 rows, 4 columns)
three_d_list = [
    [  # First matrix
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [  # Second matrix
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]
]

# Accessing an element (2nd matrix, 3rd row, 2nd column)
print(three_d_list[1][2][1])  # Output: 22

for matrix in three_d_list:
    for row in matrix:
        print(row)  # Prints each row
    print()  # Newline for separation
