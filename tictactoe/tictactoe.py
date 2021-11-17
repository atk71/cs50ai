"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = 0
    count_o = 0

    for row in board:
        count_x += row.count(X)
        count_o += row.count(O)

    return X if (count_x <= count_o) else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_spots = set()

    for i, row in enumerate(board):
        for j, spot in enumerate(row):
            if spot == EMPTY:
                available_spots.add((i, j))

    return available_spots


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action in actions(board):
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = player(new_board)
        return new_board
    else:
        raise ValueError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] is not EMPTY:
            if (board[i][0] == board[i][1]) and (board[i][0] == board[i][2]):
                return board[i][0]
        if board[0][i] is not EMPTY:
            if (board[0][i] == board[1][i]) and (board[0][i] == board[2][i]):
                return board[0][i]
    if board[1][1] is not EMPTY:
        if (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]):
            return board[1][1]
        if (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]):
            return board[1][1]

    return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return True if (winner(board) is not EMPTY or not actions(board)) else False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) not in (X, O):
        return 0
    else:
        return 1 if (winner(board) == X) else -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board):
        if terminal(board):
            return utility(board), None
        v = -math.inf
        move = None
        for action in actions(board):
            min = min_value(result(board, action))[0]
            if v < min:
                v = max(v, min)
                move = action
        return v, move

    def min_value(board):
        if terminal(board):
            return utility(board), None
        v = math.inf
        move = None
        for action in actions(board):
            max = max_value(result(board, action))[0]
            if v > max:
                v = min(v, max)
                move = action
        return v, move

    while not terminal(board):
        return max_value(board)[1] if player(board) is X else min_value(board)[1]
    return None
