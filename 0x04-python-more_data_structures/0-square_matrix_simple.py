#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    _matrix = []

    for row in matrix:
        res = list(map(lambda x: x**2, row))
        _matrix.append(res)

    return _matrix
