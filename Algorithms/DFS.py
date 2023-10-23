import time

from Algorithms.Search_Algorithm import Search_Algorithm, Solution


class DFS(Search_Algorithm):
    def __init__(self, initial_state):
        super().__init__(initial_state)

    def solve(self):
        if not self.is_solvable():
            return Solution(False)

        frontier = [self.initial_state]
        explored = set()
        parent = dict()          # Parent map its key : current_state & value : (cost of the current_state, its parent)

        search_depth = 0
        #
        initial_state_str = self.stringify_state(self.initial_state)
        parent[initial_state_str] = (0, None)

        start_time = time.perf_counter()
        print(self.initial_state, self.goal_test)

        while not len(frontier) == 0:
            current_state = frontier.pop(len(frontier) - 1)
            current_state_str = self.stringify_state(current_state)
            explored.add(current_state_str)
            print(current_state_str, "len frontier: ", len(frontier), "len explored: ", len(explored))

            if current_state == self.goal_test:
                break

            cost = parent[current_state_str][0]
            cost += 1

            x, y = self.get_empty_tile_location(current_state)

            for move in range(4):
                if not self.is_valid_move(x, y, move):
                    continue

                new_state = self.deep_copy(current_state)
                self.apply_move(new_state, x, y, move)
                new_state_str = self.stringify_state(new_state)

                if new_state_str not in explored and new_state not in frontier:
                    frontier.append(new_state)
                    parent[new_state_str] = (cost, current_state_str)
                    search_depth = max(search_depth, cost)

        end_time = time.perf_counter()

        path = self.find_path(self.goal_test, parent)
        total_time = end_time - start_time
        cost = parent[self.stringify_state(self.goal_test)][0]
        nodes_expanded = len(explored)
        return Solution(True, path, cost, nodes_expanded, search_depth, total_time)


