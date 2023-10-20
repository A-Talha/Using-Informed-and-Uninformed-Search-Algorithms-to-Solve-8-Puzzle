class Body:
    def __init__(self,starting_state):
        self.starting_state = starting_state

    def solve(self):
        pass


class Solution:
    def __init__(self,solvable,solution,steps):
        self.solvable = solvable
        self.solution = solution
        self.steps = steps

    def has_solution(self):
        return self.solvable

    def get_solution(self):
        return self.solution

    def get_steps(self):
        return self.steps