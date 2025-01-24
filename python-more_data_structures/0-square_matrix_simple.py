#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    i = 0;

    for row in matrix:
        new_row = []
        for j in range(len(row)):
           new_row.append(j * j)
        new_matrix.append(new_row)
        
    return new_matrix
