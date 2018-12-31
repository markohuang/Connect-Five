from advanced_util import *


def gomoku30(board, col):
    opp = 'ox'.replace(col, '')
    open = check_open_positions(board)
    # check if there are winning positions
    for position in open[4][col]:
        group = unpack_positions(position)
        for square in group:
            y, x = square
            if board[y][x] == ' ':
                return square
    # check if there are must-respond situations
    for position in open[4][opp]:
        group = unpack_positions(position)
        for square in group:
            y, x = square
            if board[y][x] == ' ':
                return square
    # see if there is a winning combination
    forced = forced_play(board, col)
    if forced:
        return forced[0]

    # vanilla heuristic
    score = blank_score(board)
    score = get_score(board, col, score)
    return find_best_square(score)
