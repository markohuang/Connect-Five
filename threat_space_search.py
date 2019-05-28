"""Search through threat space (Under Construction)"""
from copy import deepcopy

from get_threats import get_threats
from util import Queue


def threat_space_search(original_board, col):
    """Search all possible ways to reach a win"""
    opp = 'ox'.replace(col, '')
    board = deepcopy(original_board)
    threats = get_threats(board, col)
    frontier = Queue()
    frontier.list = [[x] for x in threats]
    visited_boards = [x for x, _ in threats]
    while not frontier.isEmpty():
        state = frontier.pop()
        board, threat = state[-1]
        if threat.is_winning_threat():
            winning_play = []
            for _, item in state:
                winning_play.append(item.gain_square)
            # str = 'mate in {}'.format(len(winning_play))
            # print(str)
            return winning_play
        successor_states = []

        # FIXME comment this out to test other functionality
        # FIXME checking for combinations DOES NOT WORK YET
        # comb_board = deepcopy(board)
        # for item in frontier.list:
        #     threat2 = item[-1][1]
        #     if threat2 == threat:
        #         continue
        #     if threat2.gain_square in threat.cost_squares:
        #         continue
        #     if threat.gain_square in threat2.cost_squares:
        #         continue
        #     valid = True
        #     for csquare in threat.cost_squares:
        #         if csquare in threat2.cost_squares:
        #             valid = False
        #             break
        #     if valid:
        #         put_on_board(comb_board, threat2.gain_square, col)
        #         for _, threat2 in item:
        #             put_on_board(comb_board, threat2.gain_square, col)
        #             for csquare in threat2.cost_squares:
        #                 put_on_board(comb_board, csquare, opp)
        # comb_threats = get_threats(comb_board, col)
        # if comb_threats:
        #     for comb_board, comb_threat in comb_threats:
        #         successor_states.append((comb_board, comb_threat))
        # FIXME end

        for item in state:
            board, threat = item
            new_threats = get_threats(board, col)
            for new_board, new_threat in new_threats:
                if threat.gain_square in new_threat.rest_squares:
                    successor_states.append((new_board, new_threat))
        for successor in successor_states:
            next_board, next_threat = successor
            if next_board not in visited_boards:
                path = state + [successor]
                frontier.push(path)
                visited_boards += [next_board]
    return False


# def get_subBoard(board, square):  # deprecated
#     y, x = square
#     init_y, init_x = (max(y-4, 0), max(x-4, 0))
#     end_y, end_x = (min(y+4, 14), min(x+4, 14))
#     new_board = board[init_y:end_y+1]
#     for i in range(len(new_board)):
#         row = new_board[i]
#         new_board[i] = row[init_x:end_x+1]
#     return new_board


# def forced_play(original_board, col):  # deprecated
#     # returns a list containing the winning combination of moves (if there are any)
#     # else returns False
#     board = deepcopy(original_board)
#     open = check_open_positions(board)
#     opp = 'ox'.replace(col, '')
#     possible_plays, _ = get_plays_available(board, open[3][col])
#     q = Queue()
#     visited = [board]
#     for play in possible_plays:
#         pos1, pos2 = play
#         next_board = copy.deepcopy(board)
#         y1, x1 = pos1
#         y2, x2 = pos2
#         next_board[y1][x1] = col
#         next_board[y2][x2] = opp
#         open = check_open_positions(next_board)
#         if open[4][opp] or open[5][opp]:
#             continue
#         q.push([(next_board, play)])
#         visited += [next_board]
#     while not q.isEmpty():
#         state = q.pop()
#         board = state[-1][0]
#         open = check_open_positions(board)
#         if open[4][col]:  # this is a winning forced playing position
#             # print_board(board)
#             # print('winning entry:', open[4][col])
#             winning_play = []
#             for item in state:
#                 play = item[1][0]
#                 winning_play.append(play)
#             str = 'mate in {}'.format(len(winning_play))
#             print(str)
#             return winning_play
#         possible_plays, _ = get_plays_available(board, open[3][col])
#         for play in possible_plays:
#             pos1, pos2 = play
#             next_board = copy.deepcopy(board)
#             y1, x1 = pos1
#             y2, x2 = pos2
#             next_board[y1][x1] = col
#             next_board[y2][x2] = opp
#             open = check_open_positions(next_board)
#             if open[4][opp] or open[5][opp]:
#                 continue
#             if next_board not in visited:
#                 path = state + [(next_board, play)]
#                 q.push(path)
#                 visited += [next_board]
#     return False
