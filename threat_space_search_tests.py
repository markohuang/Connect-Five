from deprecated.advanced_util import *
from threat_space_search import *
from util import *


# 这里的test uncomment一下然后跑一下就可以大概知道是怎么回事了
# 把function里的东西直接放到console里面跑可以print_board(board)一下
# Test 1
def test1():
    board = make_empty_board(15)
    board[4][6] = 'x'
    board[7][6] = 'o'
    board[8][6] = 'x'
    board[9][6] = 'o'
    board[7][7] = 'x'
    board[8][7] = 'x'
    board[9][7] = 'x'
    board[10][7] = 'o'
    board[8][5] = 'o'
    board[9][5] = 'x'
    board[10][4] = 'o'
    board[9][11] = 'o'
    x = threat_space_search(board, 'x')
    visualize_sol(board, x)
    return x


# Test 2
def test2():
    board = make_empty_board(15)
    board[0][0] = 'x'
    board[0][1] = 'x'
    board[0][2] = 'x'
    board[1][0] = 'x'
    board[2][0] = 'x'
    board[1][5] = 'x'
    board[2][6] = 'x'
    board[5][8] = 'x'
    board[6][8] = 'x'
    board[2][8] = 'o'
    board[9][8] = 'o'
    board[5][9] = 'o'
    board[0][12] = 'x'
    board[0][13] = 'x'
    board[0][14] = 'x'
    board[1][14] = 'x'
    board[2][14] = 'x'
    board[14][0] = 'x'
    board[14][1] = 'x'
    board[14][2] = 'x'
    board[13][0] = 'x'
    board[12][0] = 'x'
    board[14][12] = 'x'
    board[14][13] = 'x'
    board[14][14] = 'x'
    board[13][14] = 'x'
    board[12][14] = 'x'
    x = threat_space_search(board, 'x')
    visualize_sol(board, x)
    return x


# Test 3
# 有点尴尬。我并没有查什么combination就已经有解了
# 一开始以为是bug疯狂查，并没有查到，然后跟着debugger过了一遍
# 发现，额好像跟着他的解这样确实就赢了。不过我还是加一个查combination的东西吧
# 不过就缺一个只能通过combination查出解的test case
def test3():
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
    x = threat_space_search(board, 'x')
    visualize_sol(board, x)
    return x


def test4():
    board = make_empty_board(15)
    board[10][4] = 'o'
    board[6][5] = 'o'
    board[7][5] = 'o'
    board[8][5] = 'o'
    board[9][5] = 'o'
    board[10][5] = 'x'
    board[6][6] = 'x'
    board[7][6] = 'o'
    board[8][6] = 'x'
    board[9][6] = 'x'
    board[10][6] = 'x'
    board[11][6] = 'o'
    board[6][7] = 'x'
    board[7][7] = 'x'
    board[8][7] = 'x'
    board[9][7] = 'o'
    board[10][7] = 'x'
    board[6][8] = 'x'
    board[7][8] = 'o'
    board[8][8] = 'x'
    board[8][9] = 'o'
    board[9][9] = 'o'
    # x = threat_space_search(board, 'x')
    x = forced_play(board, 'x')
    visualize_sol(board, x)
    return x


def visualize_sol(board, x):
    print_board(board)
    print("--SOLUTION--")
    board2 = deepcopy(board)
    for move in x:
        board2[move[0]][move[1]] = 'x'
    print_board(board2)


if __name__ == "__main__":
    x = test2()
    y = 1
    # import time
    # start = time.time()
    # for i in range(10):
    #     x = threat_space_search(board, 'x')
    # end = time.time()
    # print((end - start) / 10)
