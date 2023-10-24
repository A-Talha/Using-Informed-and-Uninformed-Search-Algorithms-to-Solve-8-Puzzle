from Algorithms.Search_Algorithm import Search_Algorithm
from Algorithms.DFS import DFS
from Algorithms.BFS import BFS
from Algorithms.AStar import A_Star

DEFAULT_GOAL_TEST = 12345678
DEFAULT_ALGORITHM = "DFS"


def get_algorithm(initial_state, algorithm, heuristic=None, goal_test=None):
    if goal_test is None:
        goal_test = DEFAULT_GOAL_TEST

    match algorithm:
        case "DFS":
            return DFS(initial_state, goal_test)
        case "BFS":
            return BFS(initial_state, goal_test)
        case "A-Star":
            if heuristic is None:
                return Search_Algorithm(initial_state, goal_test)
            return A_Star(initial_state, goal_test, heuristic)
        case _:
            return Search_Algorithm(initial_state, goal_test)
