from abc import ABC, abstractmethod
from math import sqrt

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


class Search_Algorithm(ABC):
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.board_size = self.get_board_size()
        self.goal_test = self.set_goal_test()

    @staticmethod
    def get_empty_tile_location(state):
        return next(((x, y) for x, row in enumerate(state) for y, val in enumerate(row) if val == 0))

    @staticmethod
    def apply_move(state, x, y, move):
        state[x][y], state[x + dx[move]][y + dy[move]] = state[x + dx[move]][y + dy[move]], state[x][y]

    @staticmethod
    def deep_copy(state):
        return [row[:] for row in state]

    @staticmethod
    def stringify_state(state):
        return ",".join([",".join(map(str, row)) for row in state])

    def set_goal_test(self):
        goal_test = [[j * self.board_size + i for i in range(self.board_size)] for j in range(self.board_size)]
        return goal_test

    def get_board_size(self):
        return len(self.initial_state[0])

    def is_solvable(self):
        size = self.get_board_size()
        inversions_count = 0
        state_list = [element for sublist in self.initial_state for element in sublist]

        for i in range(size * size):
            if state_list[i] == 0:
                continue
            for j in range(i):
                if state_list[j] and state_list[i] > state_list[j]:
                    inversions_count += 1

        return inversions_count % 2 == 0

    def is_valid_move(self, x, y, move):
        return not (x + dx[move] < 0 or x + dx[move] >= self.board_size or y + dy[move] < 0 or y + dy[move] >= self.board_size)

    def find_path(self, goal_test, parent):
        path = []
        state_str = self.stringify_state(goal_test)
        while state_str:
            path.append(state_str)
            state_str = parent[state_str][1]

        path.reverse()
        return path

    @abstractmethod
    def solve(self):
        return Solution(False)


class Solution:
    def __init__(self, solvable, path=None, cost=None, nodes_expanded=None, search_depth=None, running_time=None):
        if path is None:
            path = []
        self.solvable = solvable
        self.path = path
        self.cost = cost
        self.nodes_expanded = nodes_expanded
        self.search_depth = search_depth
        self.running_time = running_time

    def exist(self):
        return self.solvable

    def stringify(self):
        if not self.exist():
            return ""
        else:
            string = "Cost: " + str(self.cost) + "\n"
            string += "Nodes expanded: " + str(self.nodes_expanded) + "\n"
            string += "Search depth: " + str(self.search_depth) + "\n"
            string += "Running time: " + f"{self.running_time:.5f} S" + "\n"
            return string

    def print(self):
        print(self.solvable)
        if not self.solvable:
            print("No solution")
        else:
            print("Path:")
            for state_index in range(len(self.path)):
                print("State", str(state_index) + ':')
                self.print_state(self.path[state_index])
            print("Cost:", self.cost)
            print("Nodes expanded:", self.nodes_expanded)
            print("Search depth:", self.search_depth)
            print("Running time:", self.running_time, "Sec")

    @staticmethod
    def print_state(state):
        state_board = state.split(",")
        board_size = int(sqrt(len(state_board)))

        for i in range(board_size):
            for j in range(board_size):
                print(state_board[i * board_size + j], end=' ')
            print()
        print()

