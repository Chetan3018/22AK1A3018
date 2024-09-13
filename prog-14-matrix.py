def interchange_first_last_columns(matrix):
    rows = len(matrix)
    if rows == 0 or len(matrix[0]) < 2:
        return matrix    # Interchange the first and last columns
    for i in range(rows):
        matrix[i][0], matrix[i][-1] = matrix[i][-1], matrix[i][0]
    return matrix
def print_matrix(matrix):
    for row in matrix:
        print(row)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
print_matrix(matrix)
interchanged_matrix = interchange_first_last_columns(matrix)
print("\nMatrix after interchanging first and last columns:")
print_matrix(interchanged_matrix)
