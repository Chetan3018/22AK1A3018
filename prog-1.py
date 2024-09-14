def add_matrices(A, B):
    result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return result

def subtract_matrices(A, B):
    result = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
    return result

def multiply_matrices(A, B):
    result = [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
    return result

def trace_matrix(A):
    return sum(A[i][i] for i in range(len(A)))
