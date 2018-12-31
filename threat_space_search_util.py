from copy import deepcopy


class Threat:
    def __init__(self, name):
        self.name = name
        self.gain_squares = []
        self.rest_squares = []
        self.cost_squares = []

    def is_winning_threat(self):
        if self.name in ['straight four', 'five']:
            return True
        return False


def put_on_board(board, pos, col):
    y, x = pos
    board[y][x] = col


def unpack_position(position, board, col, n=5):
    # helper function for get_forced_plays_available
    pos1, pos2 = position
    dy, dx = (b - a for a, b in zip(pos1, pos2))
    if dy == 0:
        group = [(pos1[0], x + pos1[1]) for x in range(n)]
    elif dx == 0:
        group = [(y + pos1[0], pos1[1]) for y in range(n)]
    elif dx < 0:
        group = [(xy + pos1[0], pos1[1] - xy) for xy in range(n)]
    else:
        group = [(xy + pos1[0], xy + pos1[1]) for xy in range(n)]
    # e.g. ((1, 6) <-start, (5, 2) <- end) -->
    # group = [(1, 6), (2, 5), (3, 4), (4, 3), (5, 2)] <- expands into all positions
    #      ((3, 2), (3, 7)) -->
    # group = [(3, 2), (3, 3), (3, 4), (3, 5), (3, 6)]
    free_positions = []
    rest_positions = []
    for square in group:
        y, x = square
        if board[y][x] == ' ':
            free_positions.append(square)
        elif board[y][x] == col:
            rest_positions.append(square)
    return free_positions, rest_positions


def check_four(threats, board, i, j, dy, dx, col, opp):
    num_of_col = 0
    valid = True
    for count in range(5):
        if board[i + dy * count][j + dx * count] == opp:
            valid = False
            break
        if board[i + dy * count][j + dx * count] == col:
            num_of_col += 1
    if num_of_col == 3 and valid:
        start_pos = (i, j)
        end_pos = (i + 4 * dy, j + 4 * dx)
        free_positions, rest_positions = \
            unpack_position((start_pos, end_pos), board, col, 5)
        for position in free_positions:
            threat = Threat('four')
            threat.rest_squares = rest_positions
            threat.gain_squares.append(position)
            for position_2 in free_positions:
                if position_2 != position:
                    threat.cost_squares.append(position_2)
            next_board = deepcopy(board)
            put_on_board(next_board, position, col)
            threats.append((next_board, threat))


def check_three(threats, board, i, j, dy, dx, col, opp):
    num_of_col = 0
    valid = True
    for count in range(5):
        if board[i + dy * count][j + dx * count] == opp:
            valid = False
            break
        if board[i + dy * count][j + dx * count] == col:
            num_of_col += 1
    if num_of_col == 3 and valid:
        start_pos = (i, j)
        end_pos = (i + 4 * dy, j + 4 * dx)
        free_positions, rest_positions = \
            unpack_position((start_pos, end_pos), board, col, 5)
        for position in free_positions:
            threat = Threat('four')
            threat.rest_squares = rest_positions
            threat.gain_squares.append(position)
            for position_2 in free_positions:
                if position_2 != position:
                    threat.cost_squares.append(position_2)
            next_board = deepcopy(board)
            put_on_board(next_board, position, col)
            threats.append((next_board, threat))