# even more helper functions
# most functions here are helper helper functions


def mapping(board):  # Deprecated
    # piece_map is a dictionary with two keys 'o' and 'x'.
    # the value of each key holds a list of tuples containing
    # all piece positions of the key's type.
    piece_map = {'o': [], 'x': []}
    for i in range(len(board)):
        for j in range(len(board)):
            col = board[i][j]
            if col != ' ':
                piece_map[col].append((i, j))
    return piece_map


def blank_score(board):
    # score is a dictionary with all the board positions and their corresponding values
    score = {}
    for i in range(len(board)):
        for j in range(len(board)):
            score[(i, j)] = 0
    return score


def find_best_square(score):
    # returns the square with the highest evaluated score
    max_score = max(list(score.values()))
    for square in score:
        if score[square] == max_score:
            return square


def unpack_positions(position):
    # helper function for get_forced_plays_available
    pos1, pos2 = position
    dy, dx = (b - a for a, b in zip(pos1, pos2))
    if dy == 0:
        group = [(pos1[0], x + pos1[1]) for x in range(5)]
    elif dx == 0:
        group = [(y + pos1[0], pos1[1]) for y in range(5)]
    elif dx < 0:
        group = [(xy + pos1[0], pos1[1] - xy) for xy in range(5)]
    else:
        group = [(xy + pos1[0], xy + pos1[1]) for xy in range(5)]
    # e.g. ((1, 6) <-start, (5, 2) <- end) -->
    # group = [(1, 6), (2, 5), (3, 4), (4, 3), (5, 2)] <- expands into all positions
    #      ((3, 2), (3, 7)) -->
    # group = [(3, 2), (3, 3), (3, 4), (3, 5), (3, 6)]
    return group




