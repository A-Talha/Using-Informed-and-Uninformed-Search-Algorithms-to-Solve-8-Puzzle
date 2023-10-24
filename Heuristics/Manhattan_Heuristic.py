BOARD_DIMENSION = 3


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def manhattan_heuristic(state):
    manhattan_sum = 0
    board_size = BOARD_DIMENSION * BOARD_DIMENSION
    for i in range(board_size):
        val = state % 10
        if val:
            manhattan_sum += manhattan_distance((board_size - 1 - i) // BOARD_DIMENSION, (board_size - 1 - i) % BOARD_DIMENSION, val // BOARD_DIMENSION, val % BOARD_DIMENSION)
        state //= 10
    return manhattan_sum
