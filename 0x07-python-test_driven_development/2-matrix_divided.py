#!/usr/bin/python3
"""
This module defines a function ``matrix_divided(matrix, div)``.

The function divides all elements of a matrix by the number passed.

"""


def matrix_divided(matrix, div):
    """Divides all elements of the matrix.

    Args:
        matrix (list): The matrix to be divided
        div (int): The number to divide

    Raise:
        TypeError: if matrix is not a list of list of integer or float
        ZeroDivisionError: if div is equal to 0

    Return:
        A new matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = []
    for i in matrix:
        list_1 = []
        for j in i:
            result = "{:.2f}".format(j / div)
            result = float(result)
            list_1.append(result)
        new_list.append(list_1)

    return new_list
