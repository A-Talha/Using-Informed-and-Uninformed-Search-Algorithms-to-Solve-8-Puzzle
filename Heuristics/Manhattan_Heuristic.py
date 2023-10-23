def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def manhattan_heuristic(state, board_size):
    manhattan_sum = 0
    for i in range(board_size):
        for j in range(board_size):
            if state[i][j]:
                manhattan_sum += manhattan_distance(i, j, state[i][j] // board_size, state[i][j] % board_size)
    return manhattan_sum
