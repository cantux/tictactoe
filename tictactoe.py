from check_win import check_win
from pprint import pprint

board = [
    ["*", "*", "*"],
    ["*", "*", "*"],
    ["*", "*", "*"]
    ]
len_r = 3
len_c = 3
checker_types = ["o", "", "x"]
# player_types = {"0": "ai", "1": "person"}


def encode_matrix():
    return "".join([str(c) for c in [b for b in board]])
#     key = {"o": 0, "*": 1, "x": 2}
#     res = 0
#     count = 1
#     for r in range(3):
#         for c in range(3):
#             res += (3 ** count) * key[board[r][c]]
#             count += 1
#     return res

def get_checker_ptr(move_count):
    return 1 if move_count & 1 else -1

def get_ai_move(move_count):
    return find_best_move(move_count, 1)[1]

memo = {}
def find_best_move(move_count, turn):
    curr_encode = encode_matrix()
    if curr_encode not in memo:
        if move_count == 9:
            return (0, (-1, -1))
        elif check_win(board):
            return (1 * turn, (-1, -1))

        curr_visited = set()
        best = float("-inf") if turn == -1 else float("inf")
        accum = 0
        found_best_move = [-1, -1]
        for r in range(len_r):
            for c in range(len_c):
                if (r,c) not in curr_visited and board[r][c] == "*":
                    curr_visited.add((r,c))
                    curr_checker_ptr = get_checker_ptr(move_count)
                    board[r][c] = checker_types[1 + curr_checker_ptr]
                    score_for_op, best_move_for_op = find_best_move(move_count + 1, turn * -1)
                    if turn == 1:
                        if score_for_op < best:
                            best = score_for_op
                            found_best_move = (r, c)
                    else:
                        if score_for_op > best:
                            best = score_for_op
                            found_best_move = [r, c]
                    board[r][c] = "*"
#         print(curr_encode)
#         print(best)
        memo[curr_encode] = (best, found_best_move)
    return memo[curr_encode][0], memo[curr_encode][1]

def get_person_move():
    row = input("enter row")
    col = input("enter col")
    return int(row), int(col)

def make_move(curr_player_type, move_count):
    if curr_player_type == "0":
        pprint(memo)
        return get_ai_move(move_count)
    elif curr_player_type == "1":
        return get_person_move()
    else:
        raise Exception("player type error")

def print_board(arr):
    for r in range(len_r):
        for c in range(len_c):
            print(arr[r][c] + " ", end="")
        print()

def game(players):
    move_count = 1
    curr_turn = 1
    curr_checker_type = checker_types[1 + curr_turn]
    curr_player_type = players[1 - curr_turn]
    while move_count < 10:
        r, c = make_move(curr_player_type, move_count)
        if r == -1:
            return "draw"
        board[r][c] = curr_checker_type
        print_board(board)
        if check_win(board):
            return "win: " + str(curr_turn)
        move_count += 1
        curr_turn *= -1
        curr_checker_type = checker_types[1 + curr_turn]
        curr_player_type = players[1 - curr_turn]

    return "draw"

def main():
    first_player = input("first player ai(0) or person(1): ")
    second_player = input("second player ai(0) or person(1): ")
    print(game([first_player, "", second_player]))

main()

