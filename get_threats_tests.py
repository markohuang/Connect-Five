"""Get threats tests"""
import time

# from deprecated.threat_space_search import *
from get_threats import get_threats
from util import print_board, str_to_board


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
    threats = get_threats(board, 'x')
    print_threats(board, threats)


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
    threats = get_threats(board, 'x')
    print_threats(board, threats)
    test_performance(board)


def test3():
    """Test 3"""
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
    threats = get_threats(board, 'x')
    print_threats(board, threats)
    test_performance(board)


def test_performance(board, num_cycles=200):
    """Clock the performance"""
    start = time.time()
    for _ in range(num_cycles):
        get_threats(board, 'x')
    end = time.time()
    print((end - start) / 200)


def print_threats(brd, threats):
    """Print out threats"""
    print_board(brd)
    for _, threat in threats:
        print('{}: {}'.format(threat.name, threat.gain_square))
        print('cost squares:', threat.cost_squares)
        print('rest squares:', threat.rest_squares, '\n')


if __name__ == "__main__":
    test1()
