#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    m_copy = matrix.copy()
    return list(map(lambda row:
                    list(map(lambda colm: colm ** 2, row)), m_copy))
