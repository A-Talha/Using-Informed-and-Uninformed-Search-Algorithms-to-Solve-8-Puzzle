# Import necessary libraries and modules
from abc import ABC, abstractmethod
from math import sqrt

# Define the dimension of the game board
BOARD_DIMENSION = 3

# Define movement directions (up, right, down, left)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


# Create an abstract base class for search algorithms
class Search_Algorithm(ABC):
    def __init__(self, initial_state, goal_test):
        self.initial_state = initial_state
        self.board_dimension = BOARD_DIMENSION
        self.goal_test = goal_test

    def get_board_dimension(self):
        return self.board_dimension

    def set_goal_test(self):
        return self.goal_test

    # Count the number of inversions in the state
    @staticmethod
    def count_inversions(state):
        inversions = 0
        state_str = str(state)
        if len(state_str) == 8:
            state_str = '0' + state_str

        for i in range(9):
            if int(state_str[i]) != 0:
                for j in range(i):
                    if int(state_str[j]) != 0 and int(state_str[i]) < int(state_str[j]):
                        inversions += 1
        return inversions % 2

    # Check if the initial state is solvable by comparing inversions
    def is_solvable(self):
        initial_state_inversions = self.count_inversions(self.initial_state)
        goal_test_inversions = self.count_inversions(self.goal_test)
        return initial_state_inversions == goal_test_inversions

    # Find the path from the initial state to the goal state using parent pointers
    def find_path(self, parent):
        path = []
        state_str = self.goal_test
        while state_str:
            path.append(state_str)
            state_str = parent[state_str][1]

        path.reverse()
        return path

    # Get the location of the empty tile in the state
    @staticmethod
    def get_empty_tile_location(state):
        count = 8
        while state:
            if state % 10 == 0:
                break
            state //= 10
            count -= 1
        return count // 3, count % 3

    # Abstract method to solve the puzzle
    @abstractmethod
    def solve(self):
        return Solution(False)

    # Check if a move is valid given the current position and the direction
    @staticmethod
    def is_valid_move(x, y, move):
        return not (x + dx[move] < 0 or x + dx[move] >= 3 or y + dy[move] < 0 or y + dy[move] >= 3)

    # Apply a move to the state
    @staticmethod
    def apply_move(state, x, y, move):
        old_index = x * 3 + y
        new_index = (x + dx[move]) * 3 + (y + dy[move])

        tile = (state // (10 ** (8 - new_index))) % 10
        state -= tile * (10 ** (8 - new_index))
        state += tile * (10 ** (8 - old_index))
        return state


# Class to represent the solution of the puzzle
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

    # Check if a solution exists
    def exist(self):
        return self.solvable

    # Convert the solution to a string
    def stringify(self):
        if not self.exist():
            return ""
        else:
            string = "Cost: " + str(self.cost) + "\n"
            string += "Nodes expanded: " + str(self.nodes_expanded) + "\n"
            string += "Search depth: " + str(self.search_depth) + "\n"
            string += "Running time: " + f"{self.running_time:.5f} s" + "\n"
            return string

    # Print the solution
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

    # Print the state of the puzzle
    @staticmethod
    def print_state(state):
        state_str = str(state)
        if len(state_str) == 8:
            state_str = '0' + state_str

        board_dimension = int(sqrt(len(state_str)))
        for i in range(board_dimension):
            for j in range(board_dimension):
                print(state_str[i * board_dimension + j], end=' ')
            print()
        print()
