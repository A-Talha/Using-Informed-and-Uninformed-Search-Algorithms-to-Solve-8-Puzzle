def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def manhattan_heuristic(state, board_size):
    manhattan_sum = 0
    size = board_size * board_size
    for i in range(size):
        val = state % 10
        if val:
            manhattan_sum += manhattan_distance((size - 1 - i) // board_size, (size - 1 - i) % board_size, val // board_size, val % board_size)
        state //= 10
    return manhattan_sum
