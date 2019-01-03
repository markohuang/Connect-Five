from copy import deepcopy


# 这是我想重新写get_threat
# 想试试无数个if statement能不能快一点 -> 但是好像比原来还慢QAQ -> 还出错QAQ
# --update，新的好像快一丢丢，但是我改一个bug他就慢一点……
# 要不先不纠结这个了，先继续搞下去吧QAQ
def get_threats(board, col):
    threats = []
    for i in range(len(board)):
        for j in range(len(board)):
            for dy, dx in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                check_square(threats, board, i, j, dy, dx, col)
    return threats


def check_square(threats, board, i, j, dy, dx, col):
    if i + 4 * dy not in range(len(board)) or j + 4 * dx not in range(len(board)):
        return None
    opp = 'ox'.replace(col, '')
    if board[i + 4 * dy][j + 4 * dx] == opp:
        return None
    if i + 5 * dy not in range(len(board)) or j + 5 * dx not in range(len(board)):
        check_five(threats, board, i, j, dy, dx, col, opp)
    elif board[i + 5 * dy][j + 5 * dx] != ' ':  # check 5
        check_five(threats, board, i, j, dy, dx, col, opp)

    elif i + 6 * dy not in range(len(board)) or j + 6 * dx not in range(len(board)):
        check_six(threats, board, i, j, dy, dx, col, opp)
    elif board[i + 6 * dy][j + 6 * dx] != ' ':  # check 5, 6
        check_six(threats, board, i, j, dy, dx, col, opp)

    else:  # check 5, 6, 7
        check_seven(threats, board, i, j, dy, dx, col, opp)


# Some helper stuff
def check_five(threats, board, i, j, dy, dx, col, opp):
    free = []
    rest = []
    first_four = [(i + k * dy, j + k * dx) for k in range(4)]
    for square in first_four:
        y, x = square
        if board[y][x] == opp:
            return None
        elif board[y][x] == col:
            rest.append(square)
        else:
            free.append(square)
    if not rest:
        return None
    if board[i + 4 * dy][j + 4 * dx] == col:
        rest.append((i + 4 * dy, j + 4 * dx))
    elif board[i + 4 * dy][j + 4 * dx] == ' ':
        free.append((i + 4 * dy, j + 4 * dx))
    if len(free) != 2 or len(rest) != 3:
        return None
    for position in free:
        threat = Threat('four')
        threat.rest_squares = rest
        threat.gain_square = position
        for position_2 in free:
            if position_2 != position:
                threat.cost_squares.append(position_2)
        next_board = deepcopy(board)
        put_on_board(next_board, position, col)
        threats.append((next_board, threat))


def check_six(threats, board, i, j, dy, dx, col, opp):
    free = []
    rest = []
    first_four = [(i + k * dy, j + k * dx) for k in range(4)]
    for square in first_four:
        y, x = square
        if board[y][x] == opp:
            return None
        elif board[y][x] == col:
            rest.append(square)
        else:
            free.append(square)
    if not rest:
        return None
    if board[i + 4 * dy][j + 4 * dx] == col:
        rest.append((i + 4 * dy, j + 4 * dx))
    elif board[i + 4 * dy][j + 4 * dx] == ' ':
        free.append((i + 4 * dy, j + 4 * dx))
    if len(free) == 2 and len(rest) == 3:
        for position in free:
            threat = Threat('four')
            threat.rest_squares = rest
            threat.gain_square = position
            for position_2 in free:
                if position_2 != position:
                    threat.cost_squares.append(position_2)
            next_board = deepcopy(board)
            put_on_board(next_board, position, col)
            threats.append((next_board, threat))
        return None
    if board[i][j] != ' ':
        return None

    free.append((i + 5 * dy, j + 5 * dx))
    if len(free) == 2 and len(rest) == 4:
        threat = Threat('straight four')
        threat.rest_squares = rest
        threat.gain_square = free[0]
        threat.cost_squares.append(free[-1])
        next_board = deepcopy(board)
        put_on_board(next_board, free[0], col)
        threats.append((next_board, threat))
        return None
    elif len(free) != 4 or len(rest) != 2:
        return None
    # check broken threes
    foo = board[i + 2 * dy][j + 2 * dx] == ' '
    bar = board[i + 3 * dy][j + 3 * dx] == ' '
    for position in free:
        if position in [(i + 5 * dy, j + 5 * dx), (i, j)]:
            continue
        elif board[i + dy][j + dx] == ' ' and position != (i+dy, j+dx):
            threat = Threat('three - single extension')
            threat.rest_squares = rest
            threat.gain_square = position
            for position_2 in free:
                if position_2 != position:
                    threat.cost_squares.append(position_2)
            next_board = deepcopy(board)
            put_on_board(next_board, position, col)
            threats.append((next_board, threat))
            continue
        if not (foo or bar):
            continue
        elif not foo and position == (i + 3 * dy, j + 3 * dx):
            continue
        elif not bar and position == (i + 2 * dy, j + 2 * dx):
            continue
        else:
            threat = Threat('three - broken')
            threat.rest_squares = rest
            threat.gain_square = position
            for position_2 in free:
                if position_2 != position:
                    threat.cost_squares.append(position_2)
            next_board = deepcopy(board)
            put_on_board(next_board, position, col)
            threats.append((next_board, threat))


def check_seven(threats, board, i, j, dy, dx, col, opp):
    free = []
    rest = []
    second_four = [(i + k * dy, j + k * dx) for k in range(1, 4)]
    for square in second_four:
        y, x = square
        if board[y][x] == opp:
            return None
        elif board[y][x] == col:
            rest.append(square)
        else:
            free.append(square)
    if not rest:
        return None
    if board[i][j] == col:
        rest.append((i, j))
    elif board[i][j] == ' ':
        free.append((i, j))
    if board[i + 4 * dy][j + 4 * dx] == col:
        rest.append((i + 4 * dy, j + 4 * dx))
    elif board[i + 4 * dy][j + 4 * dx] == ' ':
        free.append((i + 4 * dy, j + 4 * dx))
    if board[i][j] == opp:
        if len(free) != 2 or len(rest) != 2:
            return None
        if board[i + dy][j + dx] != ' ':
            return None
        for position in free:
            if position == (i + dy, j + dx):
                continue
            threat = Threat('three - single extension')
            threat.rest_squares = rest
            threat.gain_square = position
            threat.cost_squares.append((i + dy, j + dx))
            threat.cost_squares.append((i + 5 * dy, j + 5 * dx))
            threat.cost_squares.append((i + 6 * dy, j + 6 * dx))
            next_board = deepcopy(board)
            put_on_board(next_board, position, col)
            threats.append((next_board, threat))
        return None

    if len(free) == 2 and len(rest) == 3:
        for position in free:
            threat = Threat('four')
            threat.rest_squares = rest
            threat.gain_square = position
            for position_2 in free:
                if position_2 != position:
                    threat.cost_squares.append(position_2)
            next_board = deepcopy(board)
            put_on_board(next_board, position, col)
            threats.append((next_board, threat))
        return None
    if board[i][j] != ' ':
        return None

    free.append((i + 5 * dy, j + 5 * dx))
    if len(free) == 2 and len(rest) == 4:
        threat = Threat('straight four')
        threat.rest_squares = rest
        threat.gain_square = free[0]
        threat.cost_squares.append(free[-1])
        next_board = deepcopy(board)
        put_on_board(next_board, free[0], col)
        threats.append((next_board, threat))
        return None
    elif len(free) == 4 and len(rest) == 2:
        # check broken threes
        foo = board[i + 2 * dy][j + 2 * dx] == ' '
        bar = board[i + 3 * dy][j + 3 * dx] == ' '
        for position in free:
            if position in [(i + 5 * dy, j + 5 * dx), (i, j)]:
                continue
            if not (foo or bar):
                continue
            elif not foo and position == (i + 3 * dy, j + 3 * dx):
                continue
            elif not bar and position == (i + 2 * dy, j + 2 * dx):
                continue
            else:
                threat = Threat('three - broken')
                threat.rest_squares = rest
                threat.gain_square = position
                for position_2 in free:
                    if position_2 != position:
                        threat.cost_squares.append(position_2)
                next_board = deepcopy(board)
                put_on_board(next_board, position, col)
                threats.append((next_board, threat))
    if board[i + dy][j + dx] != ' ':
        return None

    free.append((i + 6 * dy, j + 6 * dx))
    if len(free) != 5 or len(rest) != 2:
        return None
    for position in free:
        if position in [(i, j), (i + dy, j + dx),
                        (i + 5 * dy, j + 5 * dx),
                        (i + 6 * dy, j + 6 * dx)]:
            continue
        threat = Threat('three - two extensions')
        threat.rest_squares = rest
        threat.gain_square = position
        threat.cost_squares.append((i + dy, j + dx))
        threat.cost_squares.append((i + 5*dy, j + 5*dx))
        next_board = deepcopy(board)
        put_on_board(next_board, position, col)
        threats.append((next_board, threat))
        return None


# Some additional helper stuff
def put_on_board(board, pos, col):
    y, x = pos
    board[y][x] = col


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
