import queue
import time

from Algorithms.Search_Algorithm import Search_Algorithm, Solution
from Heuristics.Manhattan_Heuristic import manhattan_heuristic
from Heuristics.Euclidean_Heuristic import euclidean_heuristic


# Define a class for the A* search algorithm.
class A_Star(Search_Algorithm):
    def __init__(self, initial_state, goal_test, heuristic):
        super().__init__(initial_state, goal_test)

        # Set the heuristic function based on the provided heuristic parameter.
        match heuristic:
            case "Manhattan":
                self.heuristic = manhattan_heuristic
            case "Euclidean":
                self.heuristic = euclidean_heuristic
            case _:
                pass

    def solve(self):
        # Check if the problem is solvable before attempting to solve it.
        if not self.is_solvable():
            return Solution(False)

        # Initialize data structures for the search, including a priority queue, explored set, and parent dictionary.
        frontier = queue.PriorityQueue()
        explored = dict()
        parent = dict()

        # Add the initial state to the frontier with a cost of 0 and no parent.
        frontier.put((0, self.initial_state))
        parent[self.initial_state] = (0, None)
        search_depth = 0

        # Start measuring time.
        start_time = time.time()

        while not frontier.empty():
            # Get the current state with the highest priority from the frontier.
            current_state = frontier.get()[1]
            if current_state in explored:
                continue

            # Mark the current state as explored.
            explored[current_state] = True

            # If the goal state is found, exit the loop.
            if current_state == self.goal_test:
                break

            # Get the cost of the current state and increment it.
            cost = parent.get(current_state)[0]
            cost += 1

            # Get the location of the empty tile.
            x, y = self.get_empty_tile_location(current_state)

            for move in range(4):
                # Check the validity of possible moves (up, down, left, right).
                if not self.is_valid_move(x, y, move):
                    continue

                # Apply the move to generate a new state and calculate its priority.
                new_state = self.apply_move(current_state, x, y, move)
                priority = cost + self.heuristic(new_state, self.goal_test)

                if new_state not in parent and new_state not in explored:
                    # Add the new state to the frontier with its priority and set its cost and parent.
                    frontier.put((priority, new_state))
                    parent[new_state] = (cost, current_state)
                    search_depth = max(search_depth, cost)
                elif new_state in parent:
                    if cost < parent[new_state][0]:
                        # Update the priority and parent if a better path to the state is found.
                        frontier.put((priority, new_state))
                        parent[new_state] = (cost, current_state)

        # Stop measuring time.

        end_time = time.time()

        # Calculate the path, cost, number of nodes expanded, search depth, and running time.
        path = self.find_path(parent)
        cost = parent[self.goal_test][0]
        nodes_expanded = len(explored)
        running_time = end_time - start_time

        # Return the solution.
        return Solution(True, path, cost, nodes_expanded, search_depth, running_time)
