from copy import deepcopy


class Threat:
    def __init__(self, name):
        self.name = name
        self.gain_square = ()
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


def check_five(threats, board, i, j, dy, dx, col):
    start_pos = (i, j)
    end_pos = (i + 4 * dy, j + 4 * dx)
    free_positions, rest_positions = \
        unpack_position((start_pos, end_pos), board, col, 5)
    if len(free_positions) != 2 or len(rest_positions) != 3:
        return None
    for position in free_positions:
        threat = Threat('four')
        threat.rest_squares = rest_positions
        threat.gain_square = position
        for position_2 in free_positions:
            if position_2 != position:
                threat.cost_squares.append(position_2)
        next_board = deepcopy(board)
        put_on_board(next_board, position, col)
        threats.append((next_board, threat))
    return None


def check_six(threats, board, i, j, dy, dx, col, blockage):
    check_five(threats, board, i, j, dy, dx, col)
    if board[i + 5*dy][j + 5*dx] != ' ' or board[i][j] != ' ':
        return None
    start_pos = (i, j)
    end_pos = (i+5*dy, j+5*dx)
    free_positions, rest_positions = \
        unpack_position((start_pos, end_pos), board, col, 6)
    if len(free_positions) == 2 and len(rest_positions) == 4:
        threat = Threat('straight four')
        threat.rest_squares = rest_positions
        threat.gain_square = free_positions[0]
        threat.cost_squares.append(free_positions[-1])
    elif len(free_positions) != 4 or len(rest_positions) != 2:
        return None
    # check broken threes
    foo = board[i + 2*dy][j + 2*dx] == ' '
    bar = board[i + 3*dy][j + 3*dx] == ' '
    if foo or bar:
        for position in free_positions:
            if position in [(i + 5*dy, j + 5*dx), (i, j)]:
                continue
            elif not foo and position == (i + 3*dy, j + 3*dx):
                continue
            elif not bar and position == (i + 2*dy, j + 2*dx):
                continue
            threat = Threat('three - broken')
            threat.rest_squares = rest_positions
            threat.gain_square = position
            for position_2 in free_positions:
                if position_2 != position:
                    threat.cost_squares.append(position_2)
            next_board = deepcopy(board)
            put_on_board(next_board, position, col)
            threats.append((next_board, threat))
    # check threes with single extension
    if blockage == 'all':
        return None
    elif blockage == 'end':
        if board[i + dy][j + dx] != ' ':
            return None
    elif blockage == 'start':
        if board[i + 4*dy][j + 4*dx] != ' ':
            return None
    for position in free_positions:
        if position in [(i + 5 * dy, j + 5 * dx), (i, j)]:
            continue
        threat = Threat('three - single extension')
        threat.rest_squares = rest_positions
        threat.gain_square = position
        for position_2 in free_positions:
            if position_2 != position:
                threat.cost_squares.append(position_2)
        next_board = deepcopy(board)
        put_on_board(next_board, position, col)
        threats.append((next_board, threat))


def check_seven(threats, board, i, j, dy, dx, col):
    if board[i + 6*dy][j + 6*dx] != ' ':
        check_six(threats, board, i, j, dy, dx, col, 'end')
        return None
    elif board[i][j] != ' ':
        check_six(threats, board, i, j, dy, dx, col, 'start')
        return None
    else:
        check_six(threats, board, i, j, dy, dx, col, 'all')
    if board[i + 5*dy][j + 5*dx] != ' ' or \
            board[i+dy][j+dx] != ' ':
        return None
    start_pos = (i+dy, j+dx)
    end_pos = (i+5*dy, j+5*dx)
    free_positions, rest_positions = \
        unpack_position((start_pos, end_pos), board, col, 5)
    if len(free_positions) != 3 or len(rest_positions) != 2:
        return None
    for position in free_positions:
        if position in [(i+dy, j+dx), (i+5*dy, j+5*dx)]:
            continue
        threat = Threat('three - two extensions')
        threat.rest_squares = rest_positions
        threat.gain_square = position
        for position_2 in free_positions:
            if position_2 != position:
                threat.cost_squares.append(position_2)
        next_board = deepcopy(board)
        put_on_board(next_board, position, col)
        threats.append((next_board, threat))
