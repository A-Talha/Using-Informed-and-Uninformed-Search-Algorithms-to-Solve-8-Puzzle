from abc import ABC, abstractmethod
from math import sqrt

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


class Search_Algorithm(ABC):
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.board_size = 3
        self.goal_test = 12345678

    def is_solvable(self):
        inversions = 0
        initial_state_str = str(self.initial_state)

        for i in range(9):
            if not initial_state_str[i]:
                for j in range(i):
                    if initial_state_str[j] and initial_state_str[i] < initial_state_str[j]:
                        inversions += 1
        return inversions % 2 == 0

    @staticmethod
    def get_empty_tile_location(state):
        count = 8
        while state:
            if state % 10 == 0:
                break
            state //= 10
            count -= 1

        return count // 3, count % 3

    @staticmethod
    def apply_move(state, x, y, move):
        old_index = x * 3 + y
        new_index = (x + dx[move]) * 3 + (y + dy[move])

        value_at_new = (state // (10 ** (8 - new_index))) % 10
        state -= value_at_new * (10 ** (8 - new_index))
        state += value_at_new * (10 ** (8 - old_index))
        return state

    @staticmethod
    def set_goal_test(self):
        goal_test = 12345678
        return goal_test

    @staticmethod
    def state_to_string(self,state):
        return ''.join([''.join(map(str, row)) for row in state])

    @staticmethod
    def get_board_size(self):
        return 3

    @staticmethod
    def is_valid_move(x, y, move):
        return not (x + dx[move] < 0 or x + dx[move] >= 3 or y + dy[move] < 0 or y + dy[move] >= 3)

    @staticmethod
    def find_path(parent):
        path = []
        state_str = 12345678
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
        if self.solvable:
            print("Path:")
            for state_index in range(len(self.path)):
                print("State", str(state_index) + ':')
                self.print_state(self.path[state_index])
            print("Cost:", self.cost)
            print("Nodes expanded:", self.nodes_expanded)
            print("Search depth:", self.search_depth)
            print("Running time:", self.running_time, "S")

    @staticmethod
    def print_state(state):
        state_str = str(state)
        if len(state_str) == 8:
            state_str = '0' + state_str

        board_size = int(sqrt(len(state_str)))
        for i in range(board_size):
            for j in range(board_size):
                print(state_str[i * board_size + j], end=' ')
            print()
        print()

