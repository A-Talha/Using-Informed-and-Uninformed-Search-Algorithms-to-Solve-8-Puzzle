from Algorithms.Search_Algorithm import Search_Algorithm, Solution


class DFS(Search_Algorithm):
    def __init__(self, initial_state):
        super().__init__(initial_state)

    def solve(self):
        if not self.is_solvable():
            return Solution(False)

        pass