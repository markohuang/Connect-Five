from copy import deepcopy
from threat_space_search_util import *


def get_threats(board, col):
    # threats = {'three': {'o': [], 'x': []}, 'four': {'o': [], 'x': []},
    #            'broken three': {'o': [], 'x': []},
    #            'straight four': {'o': [], 'x': []}, 'five': {'o': [], 'x': []}}
    threats = []
    opp = 'ox'.replace(col, '')
    for i in range(len(board)):
        for j in range(len(board)):
            for dy, dx in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                if i+4*dy not in range(len(board)) or j+4*dx not in range(len(board)):
                    continue
                elif i+5*dy not in range(len(board)) or j+5*dx not in range(len(board)):
                    check_four(threats, board, i, j, dy, dx, col, opp)
                    continue
                elif i+6*dy not in range(len(board)) or j+6*dx not in range(len(board)):
                    continue
                num_of_col = 0
                valid = True
                for count in range(7):
                    if count in range(1, 6):
                        if board[i+dy*count][j+dx*count] == opp:
                            valid = False
                            break
                        if board[i + dy * count][j + dx * count] == col:
                            num_of_col += 1
                if num_of_col > 0 and valid:
                    end_pos = (i + 4 * dy, j + 4 * dx)
                    open[num_of_col][col].append(((i, j), end_pos))
    return threats