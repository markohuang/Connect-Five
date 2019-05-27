"""Threat space search tests"""
from copy import deepcopy

from deprecated.advanced_util import forced_play  # for comparison
from threat_space_search import threat_space_search
from util import print_board


def test1():
    """Test 1"""
    board = str_to_board('''
*0|1|2|3|4|5|6|7|8|9|0|1|2|3|4*
0 | | | | | | | | | | | | | | *
1 | | | | | | | | | | | | | | *
2 | | | | | | | | | | | | | | *
3 | | | | | | | | | | | | | | *
4 | | | | | |x| | | | | | | | *
5 | | | | | | | | | | | | | | *
6 | | | | | | | | | | | | | | *
7 | | | | | |o|x| | | | | | | *
8 | | | | |o|x|x| | | | | | | *
9 | | | | |x|o|x| | | |o| | | *
0 | | | |o| | |o| | | | | | | *
1 | | | | | | | | | | | | | | *
2 | | | | | | | | | | | | | | *
3 | | | | | | | | | | | | | | *
4 | | | | | | | | | | | | | | *
*******************************''')
    winning_combination = threat_space_search(board, 'x')
    visualize_sol(board, winning_combination)
    return winning_combination


def test2():
    """Test 2"""
    board = str_to_board('''
*0|1|2|3|4|5|6|7|8|9|0|1|2|3|4*
0x|x|x| | | | | | | | | |x|x|x*
1x| | | | |x| | | | | | | | |x*
2x| | | | | |x| |o| | | | | |x*
3 | | | | | | | | | | | | | | *
4 | | | | | | | | | | | | | | *
5 | | | | | | | |x|o| | | | | *
6 | | | | | | | |x| | | | | | *
7 | | | | | | | | | | | | | | *
8 | | | | | | | | | | | | | | *
9 | | | | | | | |o| | | | | | *
0 | | | | | | | | | | | | | | *
1 | | | | | | | | | | | | | | *
2x| | | | | | | | | | | | | |x*
3x| | | | | | | | | | | | | |x*
4x|x|x| | | | | | | | | |x|x|x*
*******************************''')
    winning_combination = threat_space_search(board, 'x')
    visualize_sol(board, winning_combination)
    return winning_combination


def test3():
    """Test 3 FIXME: Doesn't work yet"""
    board = str_to_board('''
*0|1|2|3|4|5|6|7|8|9|0|1|2|3|4*
0 | | | | | | | | | | | | | | *
1 | | | | | | | | | | | | | | *
2 | | | | | | | | | | | | | | *
3 | | | | | | | | | | | | | | *
4 | | | | | | | | | | | | | | *
5 | | | | | |x| | | | | | | | *
6 | | | | | |o| |o|o| | | | | *
7 | | | | | |o|x| | |o| | | | *
8 | | | | | |o| |x|x| | | | | *
9 | | | | | | | | | | | | | | *
0 | | | | | | | | | | | | | | *
1 | | | | | | | | | | | | | | *
2 | | | | | | | | | | | | | | *
3 | | | | | | | | | | | | | | *
4 | | | | | | | | | | | | | | *
*******************************''')
    winning_combination = threat_space_search(board, 'x')
    visualize_sol(board, winning_combination)
    return winning_combination


def test4():
    """Test 4 FIXME: Doesn't work yet"""
    board = str_to_board('''
*0|1|2|3|4|5|6|7|8|9|0|1|2|3|4*
0 | | | | | | | | | | | | | | *
1 | | | | | | | | | | | | | | *
2 | | | | | | | | | | | | | | *
3 | | | | | | | | | | | | | | *
4 | | | | | | | | | | | | | | *
5 | | | | | | | | | | | | | | *
6 | | | | |o|x|x|x| | | | | | *
7 | | | | |o|o|x|o| | | | | | *
8 | | | | |o|x|x|x|o| | | | | *
9 | | | | |o|x|o| |o| | | | | *
0 | | | |o|x|x|x| | | | | | | *
1 | | | | | |o| | | | | | | | *
2 | | | | | | | | | | | | | | *
3 | | | | | | | | | | | | | | *
4 | | | | | | | | | | | | | | *
*******************************''')
    # winning_combination = threat_space_search(board, 'x')
    winning_combination = forced_play(board, 'x')
    visualize_sol(board, winning_combination)
    return winning_combination


def visualize_sol(board, winning_combination):
    """Visualizes the generated solution"""
    print_board(board)
    print("--SOLUTION--")
    board2 = deepcopy(board)
    for move in winning_combination:
        board2[move[0]][move[1]] = 'x'
    print(winning_combination)
    print_board(board2)


def str_to_board(board_str):
    """Turns a string into a board"""
    board = list(filter(None, board_str.replace('\n', '').split('*')))[1::]
    board = [[square for square in row[1::].split('|')] for row in board]
    return board


if __name__ == "__main__":
    test4()

    # For testing performance:
    # import time
    # start = time.time()
    # for i in range(10):
    #     x = threat_space_search(board, 'x')
    # end = time.time()
    # print((end - start) / 10)
