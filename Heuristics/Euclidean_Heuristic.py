from math import sqrt


def euclidean_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)


def euclidean_heuristic(state, board_size):
    euclidean_sum = 0
    size = board_size * board_size
    for i in range(size):
        val = state % 10
        euclidean_sum += euclidean_distance((size - 1 - i) // board_size, (size - 1 - i) % board_size, val // board_size, val % board_size)
        state //= 10
    return euclidean_sum
