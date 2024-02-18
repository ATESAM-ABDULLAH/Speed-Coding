def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if not matrix or len(matrix) == 0:  # non solvable
        return []

    ans, row_start, row_end, col_start, col_end = (
        [],
        0,
        len(matrix) - 1,
        0,
        len(matrix[0]) - 1,
    )

    while row_start <= row_end and col_start <= col_end:  # all rows and cols visited
        ans.extend(
            matrix[row_start][col_start : col_end + 1]
        )  # add top row (left->right)
        row_start += 1  # move down row
        # print("1.", ans, (rs, cs), (re, ce))

        for i in range(row_start, row_end + 1):  # add right col (top->down)
            ans.append(matrix[i][col_end])
        col_end -= 1  # move left 1 col
        # print("2.", ans, (rs, cs), (re, ce))

        if row_start <= row_end:  # add last row (right->left)
            ans.extend(matrix[row_end][col_start : col_end + 1][::-1])
            row_end -= 1  # move up 1 row
            # print("3.", ans, (rs, cs), (re, ce))

        # add left col(down->up)
        if col_start <= col_end:  # if >1 col left
            for i in range(row_end, row_start - 1, -1):
                ans.append(matrix[i][col_start])
            col_start += 1  # move right 1 col
            # print("4.", ans, (rs, cs), (re, ce))

        # print()
    return ans


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ans = spiralOrder(matrix)
print(ans)
