import queue
import time
from Method_Body import *


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def get_board_size(state):
    return len(state[0])


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def calculate_priority(x, y, move, cost):
    return manhattan_distance(0, 0, x + dx[move], y + dy[move]) + cost

#TODO: Remove this function (might help in the main file)

# def set_initial_state():
#     initial_state = [list(map(int, input().split()))]
#     board_size = get_board_size(initial_state)
#     for i in range(board_size - 1):
#         initial_state.append(list(map(int, input().split())))
#     return initial_state


def get_empty_tile(state):
    return next(((x, y) for x, row in enumerate(state) for y, val in enumerate(row) if val == 0))


def is_valid_move(x, y, move, n):
    return not (x + dx[move] < 0 or x + dx[move] >= n or y + dy[move] < 0 or y + dy[move] >= n)


def apply_move(state, x, y, move):
    state[x][y], state[x + dx[move]][y + dy[move]] = state[x + dx[move]][y + dy[move]], state[x][y]


def deep_copy(state):
    return [row[:] for row in state]


def stringify_state(state):
    return ",".join([",".join(map(str, row)) for row in state])


def find_path(goal_test, parent):
    path = []
    state_str = stringify_state(goal_test)
    while state_str:
        path.append(state_str)
        state_str = parent[state_str][1]

    path.reverse()
    return path


class Manhattan(Body):
    def __init__(self, initial_state):
        super().__init__(initial_state)

    def solve(self):
        solution = Solution(self.is_solvable())

        if not solution.solvable:
            return solution

        start_time = time.perf_counter()

        frontier = queue.PriorityQueue()
        frontier.put((0, self.initial_state))
        explored = set()
        parent = dict()

        nodes_expanded = 1
        search_depth = 0
        n = get_board_size(self.initial_state)
        parent[stringify_state(self.initial_state)] = (0, None)
        while not frontier.empty():
            _, state = frontier.get()
            state_str = stringify_state(state)
            explored.add(state_str)

            if state == self.goal_test:
                break

            x, y = get_empty_tile(state)
            cost, _ = parent[state_str]
            for move in range(4):
                if not is_valid_move(x, y, move, n):
                    continue
                new_state = deep_copy(state)
                apply_move(new_state, x, y, move)
                new_state_str = stringify_state(new_state)

                priority = calculate_priority(x, y, move, parent[state_str][0])
                if new_state_str not in parent and new_state_str not in explored:
                    frontier.put((priority, new_state))
                    parent[new_state_str] = (cost + 1, state_str)
                    search_depth = max(search_depth, cost + 1)
                    nodes_expanded += 1
                elif new_state_str in parent:
                    if cost + 1 < parent[new_state_str][0]:
                        frontier.put((calculate_priority(x, y, move, cost + 1), new_state))
                        parent[new_state_str] = (cost + 1, state_str)

        end_time = time.perf_counter()

        solution.set_path(find_path(self.goal_test, parent))
        solution.set_cost(parent[stringify_state(self.goal_test)][0])
        solution.set_nodes_expanded(nodes_expanded)
        solution.set_search_depth(search_depth)
        solution.set_running_time(end_time - start_time)
        return solution
