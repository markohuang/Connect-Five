from copy import deepcopy
from threat_space_search_util import *


# 这是个失败作品。跑一次要0.01秒
# 这个的目的是做出跟paper上跟table 1一样的表 （仅限depth 1）。
# 在advanced_util里有一个我用breadth first search写的叫forced_play的function
# 跟这个差不多，就是弱了一点，在baseline_test.py里面有一些test case可以去看一下
# 这个file的目的和forced_play差不多就是找出'x'必胜的下子顺序
# 因为这个怎么都得重写所以不用看懂细节，但是这个get_threats应该能用，在threat_space_search_test.py
# 里有一些这个function的test case
# 你可以再加一些test case试一试
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


# 这个的目的是用楼上的function写出paper里的threat space search
# 也就是找有没有forced winning combination
def get_winning_combination(threats, col):
    pass