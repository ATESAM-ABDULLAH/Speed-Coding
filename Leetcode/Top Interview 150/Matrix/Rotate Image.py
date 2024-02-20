import numpy as np


def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    # # Simple Approach
    # matrix[:] = np.transpose(matrix)  # Transpose matrix
    # matrix[:] = [list(r[::-1]) for r in matrix]  # Reverse Columns

    # Faster Approach
    row, col = len(matrix), len(matrix[0])
    for r in range(row):
        for c in range(r, col):
            # swap matrix[r][c], matrix[c][r]
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        matrix[r].reverse() # reverse cols

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
print("res = ", matrix)
