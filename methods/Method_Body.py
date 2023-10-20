from abc import ABC, abstractmethod

class Body(ABC):
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_test = self.set_goal_test()

    def set_goal_test(self):
        board_size = self.get_board_size()
        goal_test = [[j * board_size + i for i in range(board_size)] for j in range(board_size)]
        return goal_test

    def get_board_size(self):
        return len(self.initial_state[0])

    def is_solvable(self):
        size = self.get_board_size()
        inversions_count = 0

        for i in range(size):
            for j in range(size):
                if i*size + j != self.initial_state[i][j]:
                    inversions_count += 1

        return inversions_count % 2 == 0

    @abstractmethod
    def solve(self):
        pass


class Solution:
    def __init__(self, solvable):
        self.solvable = solvable
        self.path = None
        self.cost = None
        self.nodes_expanded = None
        self.search_depth = None
        self.running_time = None

    def exist(self):
        return self.solvable

    def get_path(self):
        return self.path

    def get_cost(self):
        return self.cost

    def get_nodes_expanded(self):
        return self.nodes_expanded

    def get_search_depth(self):
        return self.search_depth

    def get_running_time(self):
        return self.running_time

    def set_path(self, path):
        self.path = path

    def set_cost(self, cost):
        self.cost = cost

    def set_nodes_expanded(self, nodes_expanded):
        self.nodes_expanded = nodes_expanded

    def set_search_depth(self, search_depth):
        self.search_depth = search_depth

    def set_running_time(self, running_time):
        self.running_time = running_time