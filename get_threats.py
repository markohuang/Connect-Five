"""Examine threats for a given board"""
from copy import deepcopy
from collections import namedtuple


class Threat:
    """Threat class holds information for each threat"""
    def __init__(self, name):
        """
        name: what kind of threat is it
        gain_square: threat forms after this square is played
        rest_squares: the other squares that constitute the threat
        cost_squares: squares that the opponent can play to block the threat
        """
        self.name = name
        self.gain_square = ()
        self.rest_squares = []
        self.cost_squares = []

    def is_winning_threat(self):
        """Check whether the threat wins the game"""
        if self.name in ['straight four', 'five']:
            return True
        return False


# Basically information for a board position and a specified direction
ChessVector = namedtuple('ChessVector', 'y_index x_index delta_y delta_x')


def get_threats(board, col):
    """Goes through every square on the board checking all vector directions"""
    threats = []
    for y_index in range(len(board)):
        for x_index in range(len(board)):
            for delta_y, delta_x in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                vector = ChessVector(y_index, x_index, delta_y, delta_x)
                check_square(threats, board, vector, col)
    return threats


def check_square(threats, board, vector, col):
    """Checking a chess vector for possible threats"""
    y_index, x_index, delta_y, delta_x = \
        vector.y_index, vector.x_index, vector.delta_y, vector.delta_x
    if y_index + 4 * delta_y not in range(len(board)) or \
            x_index + 4 * delta_x not in range(len(board)):
        return
    opp = 'ox'.replace(col, '')
    if board[y_index + 4 * delta_y][x_index + 4 * delta_x] == opp:
        return
    if y_index + 5 * delta_y not in range(len(board)) or \
            x_index + 5 * delta_x not in range(len(board)):
        check_five(threats, board, vector, col, opp)
    elif board[y_index + 5 * delta_y][x_index + 5 * delta_x] != ' ':  # check 5
        check_five(threats, board, vector, col, opp)
    elif y_index + 6 * delta_y not in range(len(board)) or \
            x_index + 6 * delta_x not in range(len(board)):
        check_six(threats, board, vector, col, opp)
    elif board[y_index + 6 * delta_y][x_index + 6 * delta_x] != ' ':  # check 5, 6
        check_six(threats, board, vector, col, opp)
    else:  # check 5, 6, 7
        check_seven(threats, board, vector, col, opp)


def check_five(threats, board, vector, col, opp):
    """Checks a chess vector of length 5"""
    y_index, x_index, delta_y, delta_x = \
        vector.y_index, vector.x_index, vector.delta_y, vector.delta_x
    first_four = [(y_index + k * delta_y, x_index + k * delta_x) for k in range(4)]
    free, rest = check_kernel(first_four, board, col, opp)
    if not rest:
        return
    if board[y_index + 4 * delta_y][x_index + 4 * delta_x] == col:
        rest.append((y_index + 4 * delta_y, x_index + 4 * delta_x))
    elif board[y_index + 4 * delta_y][x_index + 4 * delta_x] == ' ':
        free.append((y_index + 4 * delta_y, x_index + 4 * delta_x))
    if len(free) == 1:
        next_board = deepcopy(board)
        threat = Threat('five')
        threat.gain_square = free[0]
        threat.rest_squares = rest
        put_on_board(next_board, free[0], col)
        threats.append((next_board, threat))
    elif len(free) != 2 or len(rest) != 3:
        return
    for position in free:
        next_board = deepcopy(board)
        threat = Threat('four')
        threat.gain_square = position
        threat.rest_squares = rest
        for position_2 in free:
            if position_2 != position:
                put_on_board(next_board, position_2, opp)
                threat.cost_squares.append(position_2)
        put_on_board(next_board, position, col)
        threats.append((next_board, threat))


def check_six(threats, board, vector, col, opp):
    """Checks a chess vector of length 6"""
    y_index, x_index, delta_y, delta_x = \
        vector.y_index, vector.x_index, vector.delta_y, vector.delta_x
    first_four = [(y_index + k * delta_y, x_index + k * delta_x) for k in range(4)]
    free, rest = check_kernel(first_four, board, col, opp)
    if not rest:
        return
    if board[y_index + 4 * delta_y][x_index + 4 * delta_x] == col:
        rest.append((y_index + 4 * delta_y, x_index + 4 * delta_x))
    elif board[y_index + 4 * delta_y][x_index + 4 * delta_x] == ' ':
        free.append((y_index + 4 * delta_y, x_index + 4 * delta_x))
    if len(free) == 2 and len(rest) == 3:
        for position in free:
            next_board = deepcopy(board)
            threat = Threat('four')
            threat.gain_square = position
            threat.rest_squares = rest
            for position_2 in free:
                if position_2 != position:
                    put_on_board(next_board, position_2, opp)
                    threat.cost_squares.append(position_2)
            put_on_board(next_board, position, col)
            threats.append((next_board, threat))
        return
    if board[y_index][x_index] != ' ':
        return

    free.append((y_index + 5 * delta_y, x_index + 5 * delta_x))
    if len(free) == 2 and len(rest) == 4:
        next_board = deepcopy(board)
        threat = Threat('straight four')
        threat.gain_square = free[0]
        threat.rest_squares = rest
        threat.cost_squares.append(free[-1])
        put_on_board(next_board, free[-1], opp)
        put_on_board(next_board, free[0], col)
        threats.append((next_board, threat))
        return
    if len(free) != 4 or len(rest) != 2:
        return
    # check broken threes
    broken_threes_case1 = board[y_index + 2 * delta_y][x_index + 2 * delta_x] == ' '
    broken_threes_case2 = board[y_index + 3 * delta_y][x_index + 3 * delta_x] == ' '
    for position in free:
        if position in [(y_index + 5 * delta_y, x_index + 5 * delta_x), (y_index, x_index)]:
            continue
        elif board[y_index + delta_y][x_index + delta_x] == ' ' and \
                position != (y_index + delta_y, x_index + delta_x):
            next_board = deepcopy(board)
            threat = Threat('three - single extension')
            threat.gain_square = position
            threat.rest_squares = rest
            for position_2 in free:
                if position_2 != position:
                    put_on_board(next_board, position_2, opp)
                    threat.cost_squares.append(position_2)
            put_on_board(next_board, position, col)
            threats.append((next_board, threat))
            continue
        if not (broken_threes_case1 or broken_threes_case2):
            continue
        elif not broken_threes_case1 and position == (y_index + 3 * delta_y, x_index + 3 * delta_x):
            continue
        elif not broken_threes_case2 and position == (y_index + 2 * delta_y, x_index + 2 * delta_x):
            continue
        else:
            next_board = deepcopy(board)
            threat = Threat('three - broken')
            threat.gain_square = position
            threat.rest_squares = rest
            for position_2 in free:
                if position_2 != position:
                    put_on_board(next_board, position_2, opp)
                    threat.cost_squares.append(position_2)
            put_on_board(next_board, position, col)
            threats.append((next_board, threat))


def check_seven(threats, board, vector, col, opp):
    """Checks a chess vector of length 7"""
    y_index, x_index, delta_y, delta_x = \
        vector.y_index, vector.x_index, vector.delta_y, vector.delta_x
    second_four = [(y_index + k * delta_y, x_index + k * delta_x) for k in range(1, 4)]
    free, rest = check_kernel(second_four, board, col, opp)
    if not rest:
        return None
    if board[y_index][x_index] == col:
        rest.append((y_index, x_index))
    elif board[y_index][x_index] == ' ':
        free.append((y_index, x_index))
    if board[y_index + 4 * delta_y][x_index + 4 * delta_x] == col:
        rest.append((y_index + 4 * delta_y, x_index + 4 * delta_x))
    elif board[y_index + 4 * delta_y][x_index + 4 * delta_x] == ' ':
        free.append((y_index + 4 * delta_y, x_index + 4 * delta_x))
    if board[y_index][x_index] == opp:
        if len(free) != 2 or len(rest) != 2:
            return None
        if board[y_index + delta_y][x_index + delta_x] != ' ':
            return None
        for position in free:
            if position == (y_index + delta_y, x_index + delta_x):
                continue
            next_board = deepcopy(board)
            threat = Threat('three - single extension')
            threat.gain_square = position
            threat.rest_squares = rest
            threat.cost_squares.append((y_index + delta_y, x_index + delta_x))
            threat.cost_squares.append((y_index + 5 * delta_y, x_index + 5 * delta_x))
            threat.cost_squares.append((y_index + 6 * delta_y, x_index + 6 * delta_x))
            put_on_board(next_board, (y_index + delta_y, x_index + delta_x), opp)
            put_on_board(next_board, (y_index + 5 * delta_y, x_index + 5 * delta_x), opp)
            put_on_board(next_board, (y_index + 6 * delta_y, x_index + 6 * delta_x), opp)
            put_on_board(next_board, position, col)
            threats.append((next_board, threat))
        return None

    if len(free) == 2 and len(rest) == 3:
        for position in free:
            next_board = deepcopy(board)
            threat = Threat('four')
            threat.gain_square = position
            threat.rest_squares = rest
            for position_2 in free:
                if position_2 != position:
                    put_on_board(next_board, position_2, opp)
                    threat.cost_squares.append(position_2)
            put_on_board(next_board, position, col)
            threats.append((next_board, threat))
        return None
    if board[y_index][x_index] != ' ':
        return None

    free.append((y_index + 5 * delta_y, x_index + 5 * delta_x))
    if len(free) == 2 and len(rest) == 4:
        next_board = deepcopy(board)
        threat = Threat('straight four')
        threat.gain_square = free[0]
        threat.rest_squares = rest
        threat.cost_squares.append(free[-1])
        put_on_board(next_board, free[-1], opp)
        put_on_board(next_board, free[0], col)
        threats.append((next_board, threat))
        return None
    if len(free) == 4 and len(rest) == 2:
        # check broken threes
        broken_threes_case1 = board[y_index + 2 * delta_y][x_index + 2 * delta_x] == ' '
        broken_threes_case2 = board[y_index + 3 * delta_y][x_index + 3 * delta_x] == ' '
        for position in free:
            if position in [(y_index + 5 * delta_y, x_index + 5 * delta_x), (y_index, x_index)]:
                continue
            if not (broken_threes_case1 or broken_threes_case2):
                continue
            elif not broken_threes_case1 and \
                    position == (y_index + 3 * delta_y, x_index + 3 * delta_x):
                continue
            elif not broken_threes_case2 and \
                    position == (y_index + 2 * delta_y, x_index + 2 * delta_x):
                continue
            else:
                next_board = deepcopy(board)
                threat = Threat('three - broken')
                threat.gain_square = position
                threat.rest_squares = rest
                for position_2 in free:
                    if position_2 != position:
                        put_on_board(next_board, position_2, opp)
                        threat.cost_squares.append(position_2)
                put_on_board(next_board, position, col)
                threats.append((next_board, threat))
    if board[y_index + delta_y][x_index + delta_x] != ' ':
        return None

    free.append((y_index + 6 * delta_y, x_index + 6 * delta_x))
    if len(free) != 5 or len(rest) != 2:
        return None
    for position in free:
        if position in [(y_index, x_index), (y_index + delta_y, x_index + delta_x),
                        (y_index + 5 * delta_y, x_index + 5 * delta_x),
                        (y_index + 6 * delta_y, x_index + 6 * delta_x)]:
            continue
        next_board = deepcopy(board)
        threat = Threat('three - two extensions')
        threat.gain_square = position
        threat.rest_squares = rest
        threat.cost_squares.append((y_index + delta_y, x_index + delta_x))
        threat.cost_squares.append((y_index + 5 * delta_y, x_index + 5 * delta_x))
        put_on_board(next_board, (y_index + delta_y, x_index + delta_x), opp)
        put_on_board(next_board, (y_index + 5 * delta_y, x_index + 5 * delta_x), opp)
        put_on_board(next_board, position, col)
        threats.append((next_board, threat))
        return None


def check_kernel(kernel_squares, board, col, opp):
    """Helper to check if the vector is worth digging deeper"""
    free, rest = [], []
    for square in kernel_squares:
        y_ind, x_ind = square
        if board[y_ind][x_ind] == opp:
            return free, rest
        if board[y_ind][x_ind] == col:
            rest.append(square)
        else:
            free.append(square)
    return free, rest


def put_on_board(board, pos, col):
    """Helper to put a square onto the board"""
    y_ind, x_ind = pos
    board[y_ind][x_ind] = col
