def square_matric_simple(matrix=[]):
    # Create a new matrix with same size as input matrix
    result_matrix = []

    for row in matrix:
        # For each row in the input matrix
        new_row = [x ** 2 for x in row]
        # Square each value in the row and append to result matrix
        result_matrix.append(new_row)

        return result_matrix
