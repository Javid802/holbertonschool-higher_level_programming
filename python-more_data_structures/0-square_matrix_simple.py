#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        row = []
        for z in range(len(matrix[i])):
            row.append(matrix[i][z]**2)
        new_matrix.append(row)
    return new_matrix
            