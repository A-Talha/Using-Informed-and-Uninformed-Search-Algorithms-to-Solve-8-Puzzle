from Algorithms.Algorithm_Factory import *
from GUI.Window import *


def main():

    AStar_Manhattan = get_algorithm([[1, 2, 3], [4, 5, 8], [6, 7, 0]], "AStar", "Manhattan")
    solution = AStar_Manhattan.solve()

    if solution.solvable:
        solution.print()
        win = Window(solution)


if __name__ == '__main__':
    main()
