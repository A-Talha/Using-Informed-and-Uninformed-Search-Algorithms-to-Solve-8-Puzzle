import time

from Algorithms.Search_Algorithm import Search_Algorithm, Solution


class DFS(Search_Algorithm):
    def __init__(self, initial_state, goal_test):
        super().__init__(initial_state, goal_test)

    def solve(self):
        # Check if the problem is solvable before attempting to solve it
        if not self.is_solvable():
            return Solution(False)

        # Initialize the frontier with the initial state
        frontier = [self.initial_state]

        # Create a set to keep track of explored states
        explored = set()

        # Create a dictionary to store the parent of each state and its cost
        parent = dict()

        # Initialize the parent of the initial state with cost 0 and no parent
        parent[self.initial_state] = (0, None)

        # Initialize the search depth
        search_depth = 0

        # Start measuring time
        start_time = time.time()

        while not len(frontier) == 0:
            # Get the current state from the frontier
            current_state = frontier.pop()

            # Mark the current state as explored
            explored.add(current_state)

            # If the goal state is found, exit the loop
            if current_state == self.goal_test:
                break

            # Get the cost of the current state
            cost = parent[current_state][0]

            # Increment the cost for the next states
            cost += 1

            # Get the location of the empty tile
            x, y = self.get_empty_tile_location(current_state)

            # Try all four possible moves
            for move in range(4):
                # Skip invalid moves
                if not self.is_valid_move(x, y, move):
                    continue

                # Apply the move to generate a new state
                new_state = self.apply_move(current_state, x, y, move)

                # If the new state has not been explored or added to the parent dictionary
                if new_state not in explored and new_state not in parent:
                    # Add the new state to the frontier
                    frontier.append(new_state)

                    # Set its cost and parent in the parent dictionary
                    parent[new_state] = (cost, current_state)

                    # Update the maximum search depth
                    search_depth = max(search_depth, cost)

        # Stop measuring time
        end_time = time.time()

        # Calculate the path, cost, number of nodes expanded, search depth, and running time
        path = self.find_path(parent)
        cost = parent[self.goal_test][0]
        nodes_expanded = len(explored)
        running_time = end_time - start_time

        # Return the solution
        return Solution(True, path, cost, nodes_expanded, search_depth, running_time)
