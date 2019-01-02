#这是我想重新写get_threat

def unpack_position(i, j, dy, dx, board, col, n=5):
    group = [(i + k*dy, j + k*dx) for k in range(n)]
    free_positions = []
    rest_positions = []
    opp_positions = []
    for square in group:
        y, x = square
        if board[y][x] == ' ':
            free_positions.append(square)
        elif board[y][x] == col:
            rest_positions.append(square)
        else:
            opp_positions.append(square)
    return free_positions, rest_positions, opp_positions


def check_seven(threats, board, i, j, dy, dx, col):
    start_pos = (i, j)
    end_pos = (i + 6 * dy, j + 6 * dx)
    free_positions, rest_positions, opp_positions = \
        unpack_position(i, j, dy, dx, board, col, 7)
