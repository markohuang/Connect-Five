# more helper functions
from Gomoku30.advanced_util2 import *
from Gomoku30.util import *
import copy


class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0


def check_open_positions(board):
    # open is a dictionary with two keys 'o' and 'x'.
    # it contains information of all the open twos, threes, and fours on the board
    # by looking at all consecutive 5-in-a-row sequences on the board
    #
    # *0|1|2|3|4|5|6|7*
    # 0 | | | | | | | *
    # 1 |o| | | | | | *
    # 2 | |o| | | | | *
    # 3 | | |o| | | | *
    # 4 | | | | | | | *
    # 5 | | | | | | | *
    # 6 | | | | | | | *
    # 7 | | | | | | | *
    # *****************
    # open = {
    # 2: {'o': [((2, 2), (6, 6))], 'x': []},
    # 3: {'o': [((0, 0), (4, 4)), ((1, 1), (5, 5))], 'x': []},
    # 4: {'o': [], 'x': []}
    # }
    #
    # The first tuple is the starting position of the open position
    # and the second tuple is the end position

    open = {1: {'o': [], 'x': []}, 2: {'o': [], 'x': []},
            3: {'o': [], 'x': []}, 4: {'o': [], 'x': []}, 5: {'o': [], 'x': []}}
    for col in ['o', 'x']:
        for i in range(len(board)):
            for j in range(len(board)):
                for dy, dx in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                    if i+4*dy not in range(len(board)) or j+4*dx not in range(len(board)):
                        continue
                    num_of_col = 0
                    valid = True
                    for count in range(5):
                        if board[i+dy*count][j+dx*count] == 'ox'.replace(col, ''):
                            valid = False
                            break
                        if board[i + dy * count][j + dx * count] == col:
                            num_of_col += 1
                    if num_of_col > 0 and valid:
                        end_pos = (i + 4 * dy, j + 4 * dx)  # end tuple of the free position
                        open[num_of_col][col].append(((i, j), end_pos))
    return open


def get_plays_available(board, positions):
    # helper function for forced_play
    # returns a list of tuples -
    # the first element of each tuple is a possible force play position
    # the second element of each tuple is a possible responsive play position
    # e.g. | |o|o|o| | --> |o|o|o|o|x| or |x|o|o|o|o|
    possible_plays = []
    free_moves = []
    for position in positions:
        group = unpack_positions(position)
        plays = []
        for square in group:
            y, x = square
            if board[y][x] == ' ':
                plays.append(square)
                free_moves.append(square)
        possible_plays.extend([tuple(plays), tuple(plays[::-1])])
    return possible_plays, set(free_moves)


def forced_play(original_board, col):
    # returns a list containing the winning combination of moves (if there are any)
    # else returns False
    board = copy.deepcopy(original_board)
    open = check_open_positions(board)
    opp = 'ox'.replace(col, '')
    possible_plays, _ = get_plays_available(board, open[3][col])
    q = Queue()
    visited = [board]
    for play in possible_plays:
        pos1, pos2 = play
        next_board = copy.deepcopy(board)
        y1, x1 = pos1
        y2, x2 = pos2
        next_board[y1][x1] = col
        next_board[y2][x2] = opp
        open = check_open_positions(next_board)
        if open[4][opp] or open[5][opp]:
            continue
        q.push([(next_board, play)])
        visited += [next_board]
    while not q.isEmpty():
        state = q.pop()
        board = state[-1][0]
        open = check_open_positions(board)
        if open[4][col]:  # this is a winning forced playing position
            # print_board(board)
            # print('winning entry:', open[4][col])
            winning_play = []
            for item in state:
                play = item[1][0]
                winning_play.append(play)
            str = 'mate in {}'.format(len(winning_play))
            print(str)
            return winning_play
        possible_plays, _ = get_plays_available(board, open[3][col])
        for play in possible_plays:
            pos1, pos2 = play
            next_board = copy.deepcopy(board)
            y1, x1 = pos1
            y2, x2 = pos2
            next_board[y1][x1] = col
            next_board[y2][x2] = opp
            open = check_open_positions(next_board)
            if open[4][opp] or open[5][opp]:
                continue
            if next_board not in visited:
                path = state + [(next_board, play)]
                q.push(path)
                visited += [next_board]
    return False


def get_score(board, col, score):
    opp = 'ox'.replace(col, '')
    open = check_open_positions(board)
    for position in open[1][col]:
        group = unpack_positions(position)
        plays = []
        for square in group:
            y, x = square
            if board[y][x] == ' ':
                plays.append(square)
        for play in plays:
            score[play] += 5
    for position in open[2][col]:
        group = unpack_positions(position)
        plays = []
        for square in group:
            y, x = square
            if board[y][x] == ' ':
                plays.append(square)
        for play in plays:
            score[play] += 25
    for position in open[3][col]:
        group = unpack_positions(position)
        plays = []
        for square in group:
            y, x = square
            if board[y][x] == ' ':
                plays.append(square)
        for play in plays:
            score[play] += 125

    for position in open[1][opp]:
        group = unpack_positions(position)
        plays = []
        for square in group:
            y, x = square
            if board[y][x] == ' ':
                plays.append(square)
        for play in plays:
            score[play] += 4
    for position in open[2][opp]:
        group = unpack_positions(position)
        plays = []
        for square in group:
            y, x = square
            if board[y][x] == ' ':
                plays.append(square)
        for play in plays:
            score[play] += 16
    for position in open[3][opp]:
        group = unpack_positions(position)
        plays = []
        for square in group:
            y, x = square
            if board[y][x] == ' ':
                plays.append(square)
        for play in plays:
            score[play] += 64
    return score
