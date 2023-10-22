from Algorithms.Algorithm_Factory import *


def main():
    AStar_Manhattan = get_algorithm([[8, 0, 6], [5, 4, 7], [2, 3, 1]], "AStar", "Manhattan")
    solution = AStar_Manhattan.solve()

    if solution.solvable:
        solution.print()


if __name__ == '__main__':
    main()
