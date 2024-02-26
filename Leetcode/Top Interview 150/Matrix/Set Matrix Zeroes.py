def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    # if len(matrix) == 0 or len(matrix[0]) == 0:
    #     return
    R, C = len(matrix), len(matrix[0])
    f_r_z, f_c_z = False, False

    for r in range(R):
        for c in range(C):
            if matrix[r][c] == 0:  # zero found

                if r == 0:  # if orig zero in first row
                    f_r_z = True
                if c == 0:  # if orig zero in first col
                    f_c_z = True

                matrix[0][c] = matrix[r][0] = (
                    0  # mark the first row and column as zeros
                )

    for r in range(R):
        for c in range(C):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if f_r_z:
        matrix[0] = [0] * C
    if f_c_z:
        matrix = [[0] + m[1:] for m in matrix]


matrix = [[1, 1, 1], [1, 1, 1], [0, 1, 1]]
setZeroes(matrix)
print(matrix)
