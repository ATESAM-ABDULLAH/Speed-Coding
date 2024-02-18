def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    1. Row/Col (1-9) no repeat
    2. 3x3 submatrix (1-9) no repeat
    """
    if not board or len(board) != 9:
        return False

    big_set = set()
    for x in range(9):  # row
        for y in range(9):  # col
            if board[x][y] == ".":  # count only filled
                continue
            if board[x][y] not in "123456789":  # exceed (1-9)
                return False
            if (
                ((x, board[x][y]) in big_set)  # unique row
                or ((board[x][y], y) in big_set)  # unique col
                or ((x // 3, y // 3, board[x][y]) in big_set)  # unique sub matrix
            ):  # check repeat
                return False
            big_set.add((x, board[x][y]))  # row stored as (row,'char')
            big_set.add((board[x][y], y))  # col stored as ('char',col)
            big_set.add(
                (x // 3, y // 3, board[x][y])
            )  # sub matrix stored as (row,col,'char')
    return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

a = isValidSudoku(board)
print(a)
