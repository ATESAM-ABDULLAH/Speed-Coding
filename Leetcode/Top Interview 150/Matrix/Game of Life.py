def gameOfLife(board):
    """
    :type board: List[List[int]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    #               left,   right,   up,    down,     lup,     ldown,    rup,   rdown
    neighbours = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    R, C = len(board), len(board[0])

    def count(board, r, c):
        count = 0
        for neighbour in neighbours:
            row, col = neighbour[0] + r, neighbour[1] + c
            if (row >= 0 and row <= R - 1) and (col >= 0 and col <= C - 1):
                if board[row][col] == 1:
                    count += 1
        return count

    flip = set()  # store all cords to flip
    for r in range(R):
        for c in range(C):
            alive = count(board, r, c)
            if board[r][c] == 1:  # alive
                if alive < 2 or alive > 3:
                    flip.add((r, c))
            else:  # dead
                if alive == 3:
                    flip.add((r, c))
    for r, c in flip:
        board[r][c] = abs(board[r][c] - 1)


board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
gameOfLife(board)
print(board)
