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

        frontier = queue.PriorityQueue()
        explored = set()
        parent = dict()

        frontier.put((0, self.initial_state))
        parent[self.initial_state] = (0, None)
        search_depth = 0
        # Initialize data structures for the search, including a priority queue, explored set, and parent dictionary.

        start_time = time.time()

        while not frontier.empty():
            current_state = frontier.get()[1]
            explored.add(current_state)

            if current_state == self.goal_test:
                break
            # Iterate while the frontier is not empty, exploring states until the goal state is reached.

            cost = parent.get(current_state)[0]
            cost += 1
            # Retrieve the current state and update the cost of reaching this state.

            x, y = self.get_empty_tile_location(current_state)
            for move in range(4):
                if not self.is_valid_move(x, y, move):
                    continue
                # Check the validity of possible moves (up, down, left, right).

                new_state = self.apply_move(current_state, x, y, move)
                priority = cost + self.heuristic(new_state, self.board_size)
                if new_state not in parent and new_state not in explored:
                    frontier.put((priority, new_state))
                    parent[new_state] = (cost, current_state)
                    search_depth = max(search_depth, cost)
                elif new_state in parent:
                    if cost < parent[new_state][0]:
                        frontier.put((priority, new_state))
                        parent[new_state] = (cost, current_state)

        end_time = time.time()

        path = self.find_path(parent)
        cost = parent[self.goal_test][0]
        nodes_expanded = len(explored)
        running_time = end_time - start_time
        return Solution(True, path, cost, nodes_expanded, search_depth, running_time)
        # Calculate path, cost, nodes expanded, search depth and running time and return the solution.
