import time
import queue

from Algorithms.Search_Algorithm import Search_Algorithm, Solution


class BFS(Search_Algorithm):
    def __init__(self, initial_state):
        super().__init__(initial_state)

    def solve(self):
        if not self.is_solvable():
            print(self.is_solvable())
            return Solution(False)

        frontier = queue.Queue()
        initial_state_str = self.stringify_state_dfs_and_bfs(self.initial_state)
        goal_state_str = self.stringify_state_dfs_and_bfs(self.goal_test)
        frontier.put(initial_state_str)
        explored = set()
        all = set()
        parent = dict()          # Parent map its key : current_state & value : (cost of the current_state, its parent)

        search_depth = 0


        parent[initial_state_str] = (0, None)

        start_time = time.perf_counter()

        while not frontier.empty():
            current_state_str = frontier.get()
            explored.add(current_state_str)
            all.add(current_state_str)

            if current_state_str == goal_state_str:
                break

            cost = parent[current_state_str][0]
            cost += 1

            x, y, zero = self.get_empty_tile_location_dfs_and_bfs(current_state_str)

            for move in range(4):
                if not self.is_valid_move(x, y, move):
                    continue
             #   print(move, "jgf",current_state_str)


                new_state_str = self.apply_move_bfs_and_dfs(current_state_str, zero, move)
              #  print(new_state_str)

                if new_state_str not in explored and new_state_str not in all:
                    all.add(new_state_str)
                    frontier.put(new_state_str)
                    parent[new_state_str] = (cost, current_state_str)
                    search_depth = max(search_depth , cost)

        end_time = time.perf_counter()
        print(end_time - start_time)
        path = self.find_path(self.goal_test, parent, True)
        total_time = end_time - start_time
        cost = parent[goal_state_str][0]
        nodes_expanded = len(explored)
        return Solution(True, path, cost, nodes_expanded, search_depth, total_time)


