def sqaure_matrix_simple(matrix=[]):
    if matrix is not None:
        return None
    return [[x **2 for x in row] for row in matrix]
