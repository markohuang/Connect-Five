from copy import deepcopy
from threat_space_search_util import *


def get_threats(board, col):
    threats = []
    # opp = 'ox'.replace(col, '')
    for i in range(len(board)):
        for j in range(len(board)):
            for dy, dx in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                if i+4*dy not in range(len(board)) or j+4*dx not in range(len(board)):
                    continue
                elif i+5*dy not in range(len(board)) or j+5*dx not in range(len(board)):
                    check_five(threats, board, i, j, dy, dx, col)
                    continue
                elif i+6*dy not in range(len(board)) or j+6*dx not in range(len(board)):
                    check_six(threats, board, i, j, dy, dx, col, 'end')
                    continue
                check_seven(threats, board, i, j, dy, dx, col)
    return threats

def get_winning_combination(threats, col):
    pass