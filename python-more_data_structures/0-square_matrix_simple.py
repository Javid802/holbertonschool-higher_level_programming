#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in range(len(matrix)):
        for z in range(len(matrix[i])):
            matrix[i][z]**=2
    return matrix
            