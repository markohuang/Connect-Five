from Gomoku30.gomoku30 import gomoku30
from Gomoku30.advanced_util import *
import random
import heapq
import copy


def is_empty(board):
    return board == make_empty_board(len(board))


def is_bounded(board, y_end, x_end, length, d_y, d_x):
    result = ["CLOSED", "SEMIOPEN", "OPEN"]
    semi_result = 0
    if y_end - length * d_y not in range(0, len(board)) or \
            x_end - length * d_x not in range(0, len(board)):
        stone1 = None
    else:
        stone1 = board[y_end - length * d_y][x_end - length * d_x]
    if y_end + d_y not in range(0, len(board)) or \
            x_end + d_x not in range(0, len(board)):
        stone2 = None
    else:
        stone2 = board[y_end + d_y][x_end + d_x]
    if stone1 == " ":
        semi_result += 1
    if stone2 == " ":
        semi_result += 1
    return result[semi_result]


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    count = 0
    end_positions = []
    result = []
    i = 0
    while y_start + i * d_y in range(len(board)) \
            and x_start + i * d_x in range(len(board)):
        if board[y_start + i * d_y][x_start + i * d_x] == col:
            count += 1
        else:
            if count == length:
                end_positions.append(i - 1)
            count = 0
        i += 1
    if count == length:
        end_positions.append(i - 1)
    for j in end_positions:
        result.append(is_bounded \
                          (board, y_start + j * d_y, x_start + j * d_x, length, d_y, d_x))
    open_seq_count = result.count("OPEN")
    semi_open_seq_count = result.count("SEMIOPEN")
    return open_seq_count, semi_open_seq_count


def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0
    for i in range(len(board)):
        open_seq_count += detect_row(board, col, i, 0, length, 0, 1)[0]
        semi_open_seq_count += detect_row(board, col, i, 0, length, 0, 1)[1]
        open_seq_count += detect_row(board, col, 0, i, length, 1, 0)[0]
        semi_open_seq_count += detect_row(board, col, 0, i, length, 1, 0)[1]
        open_seq_count += detect_row(board, col, 0, i, length, 1, 1)[0]
        semi_open_seq_count += detect_row(board, col, 0, i, length, 1, 1)[1]
        if i != 0:
            open_seq_count += detect_row(board, col, i, 0, length, 1, 1)[0]
            semi_open_seq_count += detect_row(board, col, i, 0, length, 1, 1)[1]
        open_seq_count += detect_row(board, col, 0, i, length, 1, -1)[0]
        semi_open_seq_count += detect_row(board, col, 0, i, length, 1, -1)[1]
        if i != 0:
            open_seq_count += \
                detect_row(board, col, i, len(board) - 1, length, 1, -1)[0]
            semi_open_seq_count += \
                detect_row(board, col, i, len(board) - 1, length, 1, -1)[1]
    return open_seq_count, semi_open_seq_count


def search_max(board):
    semi_result = [-100001] * (len(board) * (len(board)))
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != " ":
                continue
            board[i][j] = 'x'
            semi_result[i * len(board) // 2 // 2 + len(board) // 2 + j] = score(board)
            board[i][j] = " "
    result = semi_result.index(max(semi_result))
    move_y = result // len(board)
    move_x = result % len(board)
    print(move_y, move_x)
    return move_y, move_x


def score(board):
    MAX_SCORE = 100000
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, 'x', i)
        open_w[i], semi_open_w[i] = detect_rows(board, 'o', i)
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
    return (-10000 * (open_w[4] + semi_open_w[4]) +
            500 * open_b[4] +
            50 * semi_open_b[4] +
            -100 * open_w[3] +
            -30 * semi_open_w[3] +
            50 * open_b[3] +
            10 * semi_open_b[3] +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def detect_row_include_closed(board, col, y_start, x_start, length, d_y, d_x):
    count = 0
    end_positions = []
    result = []
    i = 0
    while y_start + i * d_y in range(len(board)) \
            and x_start + i * d_x in range(len(board)):
        if board[y_start + i * d_y][x_start + i * d_x] == col:
            count += 1
        else:
            if count == length:
                end_positions.append(i - 1)
            count = 0
        i += 1
    if count == length:
        end_positions.append(i - 1)
    for j in end_positions:
        result.append(is_bounded \
                          (board, y_start + j * d_y, x_start + j * d_x, length, d_y, d_x))
    open_seq_count = result.count("OPEN")
    semi_open_seq_count = result.count("SEMIOPEN")
    closed_seq_count = result.count("CLOSED")
    return open_seq_count, semi_open_seq_count, closed_seq_count


def detect_rows_include_closed(board, col, length):
    open_seq_count, semi_open_seq_count, closed_seq_count = 0, 0, 0
    for i in range(len(board)):
        open_seq_count += detect_row_include_closed \
            (board, col, i, 0, length, 0, 1)[0]
        semi_open_seq_count += detect_row_include_closed \
            (board, col, i, 0, length, 0, 1)[1]
        closed_seq_count += detect_row_include_closed \
            (board, col, i, 0, length, 0, 1)[2]

        open_seq_count += detect_row_include_closed \
            (board, col, 0, i, length, 1, 0)[0]
        semi_open_seq_count += detect_row_include_closed \
            (board, col, 0, i, length, 1, 0)[1]
        closed_seq_count += detect_row_include_closed \
            (board, col, 0, i, length, 1, 0)[2]

        open_seq_count += detect_row_include_closed \
            (board, col, 0, i, length, 1, 1)[0]
        semi_open_seq_count += detect_row_include_closed \
            (board, col, 0, i, length, 1, 1)[1]
        closed_seq_count += detect_row_include_closed \
            (board, col, 0, i, length, 1, 1)[2]
        if i != 0:
            open_seq_count += detect_row_include_closed \
                (board, col, i, 0, length, 1, 1)[0]
            semi_open_seq_count += detect_row_include_closed \
                (board, col, i, 0, length, 1, 1)[1]
            closed_seq_count += detect_row_include_closed \
                (board, col, i, 0, length, 1, 1)[2]

        open_seq_count += detect_row_include_closed \
            (board, col, 0, i, length, 1, -1)[0]
        semi_open_seq_count += detect_row_include_closed \
            (board, col, 0, i, length, 1, -1)[1]
        closed_seq_count += detect_row_include_closed \
            (board, col, 0, i, length, 1, -1)[2]
        if i != 0:
            open_seq_count += detect_row_include_closed \
                (board, col, i, len(board) - 1, length, 1, -1)[0]
            semi_open_seq_count += detect_row_include_closed \
                (board, col, i, len(board) - 1, length, 1, -1)[1]
            closed_seq_count += detect_row_include_closed \
                (board, col, i, len(board) - 1, length, 1, -1)[2]
    return open_seq_count, semi_open_seq_count, closed_seq_count


def is_win(board):
    if detect_rows_include_closed(board, 'x', 5) != (0, 0, 0):
        return "Black won"
    if detect_rows_include_closed(board, 'o', 5) != (0, 0, 0):
        return "White won"
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                return "Continue playing"
    return "Draw"


def print_board(board):
    s = "*"
    for i in range(len(board[0]) - 1):
        s += str(i % 10) + "|"
    s += str((len(board[0]) - 1) % 10)
    s += "*\n"
    for i in range(len(board)):
        s += str(i % 10)
        for j in range(len(board[0]) - 1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0]) - 1])
        s += "*\n"
    s += (len(board[0]) * 2 + 1) * "*"
    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "] * sz)
    return board


def analysis(board):
    for c, full_name in [['x', "Black"], ['o', "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))


def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    results = list()

    x, y = int((random.random() - 0.5) * len(board) // 4 + len(board) // 2), int(
        (random.random() - 0.5) * len(board) // 4 + len(board) // 2)
    board[y][x] = 'x'
    x, y = int((random.random() - 0.5) * len(board) // 4 + len(board) // 2), int(
        (random.random() - 0.5) * len(board) // 4 + len(board) // 2)
    while board[y][x] != " ":
        x, y = int((random.random() - 0.5) * len(board) // 4 + len(board) // 2), int(
            (random.random() - 0.5) * len(board) // 4 + len(board) // 2)
    board[y][x] = 'x'
    x, y = int((random.random() - 0.5) * len(board) // 4 + len(board) // 2), int(
        (random.random() - 0.5) * len(board) // 4 + len(board) // 2)
    while board[y][x] != " ":
        x, y = int((random.random() - 0.5) * len(board) // 4 + len(board) // 2), int(
            (random.random() - 0.5) * len(board) // 4 + len(board) // 2)
    board[y][x] = 'o'

    while True:
        print_board(board)
        # move_y, move_x = johns_ai.get_move(board,'o')
        move_x = int(input('x:\n'))
        move_y = int(input('y:\n'))
        results.append((move_y, move_x))
        print("Your Move: (%d, %d)" % (move_y, move_x))

        board[move_y][move_x] = 'o'
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            print(game_res)
            print_board(board)
            print(results)
            return game_res
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            temp = copy.deepcopy(board)
            move_y, move_x = gomoku30(board, 'x')
            board = temp
            results.append((move_y, move_x))
        print("Computer's move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = 'x'
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            print(game_res)
            print_board(board)
            print(results)
            return game_res


def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def run_test(actual, expected):
    if expected == actual:
        return "passed, %s" % (actual)
    else:
        return "failed, %s" % (actual)


def count_check(board, col):
    dctn = dict()
    for i in range(len(board)):
        for j in range(len(board)):
            for dy, dx in [(1, 0), (0, 1), (1, 1), (1, -1)]:
                if i + 4 * dy not in range(len(board)) or j + 4 * dx not in range(len(board)):
                    continue
                valid = False
                num_of_col = 0
                temp = list()
                for count in range(5):
                    if board[i + dy * count][j + dx * count] == 'wb'.replace(col, ''):
                        valid = False
                        break
                    if board[i + dy * count][j + dx * count] == ' ':
                        temp.append((i + dy * count, j + dx * count))
                    if board[i + dy * count][j + dx * count] == col:
                        valid = True
                        num_of_col += 1
                if valid:
                    try:
                        dctn[num_of_col].append([(i, j), (dy, dx), temp])
                    except:
                        dctn[num_of_col] = [[(i, j), (dy, dx), temp]]
    print(dctn)


class Stack:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Push 'item' onto the stack"
        self.list.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the stack is empty"
        return len(self.list) == 0


class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0


class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.

      Note that this PriorityQueue does not allow you to change the priority
      of an item.  However, you may insert the same item multiple times with
      different priorities.
    """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        # entry = (priority, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        #  (_, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0
