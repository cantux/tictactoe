
def inbound(r, c):
    return (0 <= r < 3) and (0 <= c < 3)
def check_win(board):
    # diagonal 2
    prev = board[0][0]
    win = prev != "*"
    for rc in range(1,3):
        win &= (board[rc][rc] != "*") and (board[rc][rc] == prev)
    if win:
        return True

    prev = board[0][2]
    win = prev != "*"
    offset = (1, -1)
    r, c = 1, 1
    while inbound(r,c):
        win &= (board[r][c] != "*") and (board[r][c] == prev)
        r, c = r + offset[0], c + offset[1]
    if win:
        return True

    # vertical 
    for c in range(3):
        prev = board[0][c]
        win = prev != "*" 
        for r in range(1,3):
            win &= (board[r][c] != "*") and (board[r][c] == prev)
        if win:
            return True

    # horizontal
    for r in range(3):
        prev = board[r][0]
        win = prev != "*"
        for c in range(1, 3):
            win &= (board[r][c] != "*") and (board[r][c] == prev)

        if win:
            return True
    return False


def check_win_test():
    diag_win11 = [
            ["x", "*", "*"],
            ["*", "x", "*"],
            ["*", "*", "x"]
            ]
    assert check_win(diag_win11)
    diag_win21 = [
            ["*", "*", "x"],
            ["*", "x", "*"],
            ["x", "*", "*"]
            ]
    assert check_win(diag_win21)
    column_win11 = [
            ["o", "*", "x"],
            ["o", "x", "*"],
            ["o", "*", "*"]
            ]
    assert check_win(column_win11)
    column_win13 = [
            ["o", "*", "x"],
            ["x", "o", "x"],
            ["o", "*", "x"]
            ]
    assert check_win(column_win13)
    row_win11 = [
            ["o", "o", "o"],
            ["x", "x", "*"],
            ["o", "*", "*"]
            ]
    assert check_win(row_win11)
    row_win12 = [
            ["x", "*", "x"],
            ["o", "o", "o"],
            ["o", "*", "*"]
            ]
    assert check_win(row_win12)
    no_winx = [
            ["x", "*", "x"],
            ["o", "o", "x"],
            ["x", "*", "*"]
            ]
    assert not check_win(no_winx)
    no_win0 = [
            ["*", "*", "*"],
            ["*", "*", "*"],
            ["*", "*", "*"]
            ]
    def check_multi(board, move_count):
        assert not check_win(board)
        if move_count == 2:
            return
        for r in range(3):
            for c in range(3):
                board[r][c] = "x"
                check_multi(board, move_count + 1)
                board[r][c] = "*"
    check_multi(no_win0, 0)


if __name__ == "__main__":
    check_win_test()





    


