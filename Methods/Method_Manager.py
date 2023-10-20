from BFS import *
from DFS import *
from Manhattan_Heuristic import *
from Euclidean_Heuristic import *


def manager(initial_state, method):
    match method:
        case "BFS":
            return BFS(initial_state)
        case "DFS":
            return DFS(initial_state)
        case "Manhattan":
            return Manhattan(initial_state)
        case "Euclidean":
            return Euclidean(initial_state)
        case _:
            pass

