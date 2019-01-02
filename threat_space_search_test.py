from threat_space_search import *
from util import *


def print_threats(brd, threats):
    print_board(brd)
    for _, threat in threats:
        print('{}: {}'.format(threat.name, threat.gain_square))
        print('cost squares:', threat.cost_squares)
        print('rest squares:', threat.rest_squares, '\n')

# 这里的test uncomment一下然后跑一下就可以大概知道是怎么回事了
# Test 1
# board = make_empty_board(15)
# board[4][6] = 'x'
# board[7][6] = 'o'
# board[8][6] = 'x'
# board[9][6] = 'o'
# board[7][7] = 'x'
# board[8][7] = 'x'
# board[9][7] = 'x'
# board[10][7] = 'o'
# board[8][5] = 'o'
# board[9][5] = 'x'
# board[10][4] = 'o'
# board[9][11] = 'o'
# x = get_threats(board, 'x')
# print_threats(board, x)

# Test 2
# board = make_empty_board(15)
# board[0][0] = 'x'
# board[0][1] = 'x'
# board[0][2] = 'x'
# board[1][0] = 'x'
# board[2][0] = 'x'
# board[1][5] = 'x'
# board[2][6] = 'x'
# board[5][8] = 'x'
# board[6][8] = 'x'
# board[2][8] = 'o'
# board[9][8] = 'o'
# board[5][9] = 'o'
# board[0][12] = 'x'
# board[0][13] = 'x'
# board[0][14] = 'x'
# board[1][14] = 'x'
# board[2][14] = 'x'
# board[14][0] = 'x'
# board[14][1] = 'x'
# board[14][2] = 'x'
# board[13][0] = 'x'
# board[12][0] = 'x'
# board[14][12] = 'x'
# board[14][13] = 'x'
# board[14][14] = 'x'
# board[13][14] = 'x'
# board[12][14] = 'x'
# x = get_threats(board, 'x')
# print_threats(board, x)

# Test 3
board = make_empty_board(15)
board[5][6] = 'x'
board[6][6] = 'o'
board[7][6] = 'o'
board[8][6] = 'o'
board[7][7] = 'x'
board[6][8] = 'o'
board[8][8] = 'x'
board[6][9] = 'o'
board[8][9] = 'x'
board[7][10] = 'o'
x = get_threats(board, 'x')
print_threats(board, x)



import time
start = time.time()
x = get_threats(board, 'x')
end = time.time()
print(end-start)