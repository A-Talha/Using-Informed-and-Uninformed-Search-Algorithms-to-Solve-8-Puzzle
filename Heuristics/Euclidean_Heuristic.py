from math import sqrt


def euclidean_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)


def euclidean_heuristic(state, board_size):
    euclidean_sum = 0
    for i in range(board_size):
        for j in range(board_size):
            euclidean_sum += euclidean_distance(i, j, state[i][j] // board_size, state[i][j] % board_size)
    return euclidean_sum
