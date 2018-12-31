from advanced_util import *

if __name__ == "__main__":
    '''
    board = make_empty_board(8)
    board[1][1] = 'o'
    board[2][2] = 'o'
    board[3][3] = 'o'
    print_board(board)
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
    # 
    print(check_open_positions(board))
    
    # open = {
    # 2: {'o': [((2, 2), (6, 6))], 'x': []}, 
    # 3: {'o': [((0, 0), (4, 4)), ((1, 1), (5, 5))], 'x': []}, 
    # 4: {'o': [], 'x': []}
    # }

    
    print(get_plays_available(board, check_open_positions(board)[3]['o']))
     
    # -> 
    # [((0, 0), (4, 4)), ((4, 4), (0, 0)), ((4, 4), (5, 5)), ((5, 5), (4, 4))]
    '''

    # forced_play test #1
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


    print_board(board)
    # print(get_plays_available(board, check_open_positions(board)[3]['x']))
    # [((3, 0), (4, 0)), ((4, 0), (3, 0)), ((0, 3), (0, 4)), ((0, 4), (0, 3))],
    # {(3, 0), (0, 3), (0, 4), (4, 0)}
    #
    # *0|1|2|3|4|5|6|7|8|9|0|1|2|3|4*
    # 0x|x|x| | | | | | | | | | | | *
    # 1x| | | | |x| | | | | | | | | *
    # 2x| | | | | |x| |o| | | | | | *
    # 3 | | | | | | | | | | | | | | *
    # 4 | | | | | | | | | | | | | | *
    # 5 | | | | | | | |x|o| | | | | *
    # 6 | | | | | | | |x| | | | | | *
    # 7 | | | | | | | | | | | | | | *
    # 8 | | | | | | | | | | | | | | *
    # 9 | | | | | | | |o| | | | | | *
    # 0 | | | | | | | | | | | | | | *
    # 1 | | | | | | | | | | | | | | *
    # 2 | | | | | | | | | | | | | | *
    # 3 | | | | | | | | | | | | | | *
    # 4 | | | | | | | | | | | | | | *
    # *******************************
    print(forced_play(board, 'x'))

    # forced_play test #2
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

    print_board(board)
    print(forced_play(board, 'x'))
    # [(5, 7), (6, 8), (3, 5)]

    # forced_play test #3
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
    print(forced_play(board, 'x'))
