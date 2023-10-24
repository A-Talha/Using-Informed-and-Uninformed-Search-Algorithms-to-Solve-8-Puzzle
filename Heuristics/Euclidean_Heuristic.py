from math import sqrt

BOARD_DIMENSION = 3


def euclidean_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)


def euclidean_heuristic(state):
    euclidean_sum = 0
    board_size = BOARD_DIMENSION * BOARD_DIMENSION
    for i in range(board_size):
        val = state % 10
        euclidean_sum += euclidean_distance((board_size - 1 - i) // BOARD_DIMENSION, (board_size - 1 - i) % BOARD_DIMENSION, val // BOARD_DIMENSION, val % BOARD_DIMENSION)
        state //= 10
    return euclidean_sum
