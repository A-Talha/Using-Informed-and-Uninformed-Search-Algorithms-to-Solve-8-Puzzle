import queue
import time

from Algorithms.Search_Algorithm import Search_Algorithm, Solution
from Heuristics.Manhattan_Heuristic import manhattan_heuristic
from Heuristics.Euclidean_Heuristic import euclidean_heuristic


# Import necessary modules and classes for the A* search algorithm.

class A_Star(Search_Algorithm):
    def __init__(self, initial_state, heuristic):
        super().__init__(initial_state)

        match heuristic:
            case "Manhattan":
                self.heuristic = manhattan_heuristic
            case "Euclidean":
                self.heuristic = euclidean_heuristic
            case _:
                pass
        # Initialize the A* search algorithm with the initial state and the selected heuristic function.

    def solve(self):
        if not self.is_solvable():
            return Solution(False)
        # Check if the initial state is solvable; if not, return a failed solution.

        start_time = time.perf_counter()

        frontier = queue.PriorityQueue()
        frontier.put((0, self.initial_state))
        explored = set()
        parent = dict()

        search_depth = 0
        initial_state_str = self.stringify_state(self.initial_state)
        parent[initial_state_str] = (0, None)
        # Initialize data structures for the search, including a priority queue, explored set, and parent dictionary.

        while not frontier.empty():
            state = frontier.get()[1]
            state_str = self.stringify_state(state)
            explored.add(state_str)

            if state == self.goal_test:
                break
            # Iterate while the frontier is not empty, exploring states until the goal state is reached.

            x, y = self.get_empty_tile_location(state)
            cost = parent.get(state_str)[0]
            cost += 1
            # Retrieve the current state and update the cost of reaching this state.

            for move in range(4):
                if not self.is_valid_move(x, y, move):
                    continue
                # Check the validity of possible moves (up, down, left, right).

                new_state = self.deep_copy(state)
                self.apply_move(new_state, x, y, move)
                new_state_str = self.stringify_state(new_state)
                # Create a new state by applying a valid move to the current state.

                priority = cost + self.heuristic(new_state, self.board_size)
                if new_state_str not in parent and new_state_str not in explored:
                    frontier.put((priority, new_state))
                    parent[new_state_str] = (cost, state_str)
                    search_depth = max(search_depth, cost)
                # Add the new state to the frontier and the parent map if it is not already explored or in the frontier.
                elif new_state_str in parent:
                    if cost < parent[new_state_str][0]:
                        frontier.put((priority, new_state))
                        parent[new_state_str] = (cost, state_str)
                # Add the state to the frontier and updating the parent map if it provides a better path.

        end_time = time.perf_counter()

        path = self.find_path(self.goal_test, parent, False)
        cost = parent[self.stringify_state(self.goal_test)][0]
        nodes_expanded = len(explored)
        running_time = end_time - start_time
        return Solution(True, path, cost, nodes_expanded, search_depth, running_time)
        # Calculate path, cost, nodes expanded, search depth and running time and return the solution.
