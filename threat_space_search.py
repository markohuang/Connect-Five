from get_threats import *
from copy import deepcopy
from util import Queue

# 还在建设中……
def threat_space_search(original_board, col):
    opp = 'ox'.replace(col, '')
    board = deepcopy(original_board)
    threats = get_threats(board, col)
    open = Queue()
    open.list = [[x] for x in threats]
    visited = [x for x, _ in threats]
    while not open.isEmpty():
        state = open.pop()
        board, threat = state[-1]
        if threat.is_winning_threat():
            winning_play = []
            for _, item in state:
                winning_play.append(item.gain_square)
            str = 'mate in {}'.format(len(winning_play))
            print(str)
            return winning_play
        successor_states = []
        for item in state:
            board, threat = item
            sub_board = get_subBoard(board, threat.gain_square)
            new_threats = get_threats(sub_board, col)
            for _, other_threat in new_threats:
                if other_threat not in state:
                    successor_states.append(other_threat)
        for threat in successor_states:
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


    for item in threats:
        board, threat = item
        sub_board = get_subBoard(board, threat.gain_square)
        new_threats = get_threats(sub_board, col)
        for _, other_threat in new_threats:
            if other_threat not in threats:



def get_subBoard(board, square):
    y, x = square
    init_y, init_x = (max(y-4, 0), max(x-4, 0))
    end_y, end_x = (min(y+4, 14), min(x+4, 14))
    new_board = board[init_y:end_y+1]
    for i in range(len(new_board)):
        row = new_board[i]
        new_board[i] = row[init_x:end_x+1]
    return new_board


def forced_play(original_board, col):
    # returns a list containing the winning combination of moves (if there are any)
    # else returns False
    board = deepcopy(original_board)
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