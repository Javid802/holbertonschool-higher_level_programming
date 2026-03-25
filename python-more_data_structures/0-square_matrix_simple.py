#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix
    for i in range(len(new_matrix)):
        for z in range(len(new_matrix[i])):
            matrix[i][z]**=2
    return new_matrix
            