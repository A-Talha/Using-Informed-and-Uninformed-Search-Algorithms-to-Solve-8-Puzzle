from Algorithms.Search_Algorithm import Search_Algorithm
from Algorithms.DFS import DFS
from Algorithms.BFS import BFS
from Algorithms.AStar import A_Star


def get_algorithm(initial_state, algorithm, heuristic=None):
    match algorithm:
        case "DFS":
            return DFS(initial_state)
        case "BFS":
            return BFS(initial_state)
        case "A-Star":
            if heuristic is None:
                return Search_Algorithm(initial_state)
            return A_Star(initial_state, heuristic)
        case _:
            return Search_Algorithm(initial_state)
