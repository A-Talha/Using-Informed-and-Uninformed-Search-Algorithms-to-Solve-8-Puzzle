from BFS import *
from DFS import *
from Manhattan_Heuristic import *
from Euclidean_Heuristic import *


def manger(starting_state,method):
    match method:
        case "BFS":
            return BFS(starting_state)
        case "DFS":
            return DFS(starting_state)
        case "Manhattan":
            return Manhattan(starting_state)
        case "Euclidean":
            return Euclidean(starting_state)
        case _:
            pass

