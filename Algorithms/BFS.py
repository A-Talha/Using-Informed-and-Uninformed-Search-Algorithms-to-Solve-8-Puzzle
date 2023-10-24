import time
import queue

from Algorithms.Search_Algorithm import Search_Algorithm, Solution


class BFS(Search_Algorithm):
    def __init__(self, initial_state):
        super().__init__(initial_state)

    def solve(self):
        if not self.is_solvable():
            return Solution(False)

        frontier = queue.Queue()
        explored = set()
        parent = dict()  # Parent map its key : current_state & value : (cost of the current_state, its parent)

        frontier.put(self.initial_state)
        parent[self.initial_state] = (0, None)
        search_depth = 0

        start_time = time.time()

        while not frontier.empty():
            current_state = frontier.get()
            explored.add(current_state)

            if current_state == self.goal_test:
                break

            cost = parent[current_state][0]
            cost += 1

            x, y = self.get_empty_tile_location(current_state)
            for move in range(4):
                if not self.is_valid_move(x, y, move):
                    continue

                new_state = self.apply_move(current_state, x, y, move)
                if new_state not in explored and new_state not in parent:
                    frontier.put(new_state)
                    parent[new_state] = (cost, current_state)
                    search_depth = max(search_depth, cost)

        end_time = time.time()

        path = self.find_path(parent)
        cost = parent[self.goal_test][0]
        nodes_expanded = len(explored)
        running_time = end_time - start_time
        return Solution(True, path, cost, nodes_expanded, search_depth, running_time)
