from Algorithms.Algorithm_Factory import *
from GUI.Window import *


def main():

    AStar_Manhattan = get_algorithm([[8, 0, 6], [5, 4, 7], [2, 3, 1]], "BFS")
    solution = AStar_Manhattan.solve()

    if solution.solvable:
        solution.print()
        win = Window(solution)


if __name__ == '__main__':
    main()
