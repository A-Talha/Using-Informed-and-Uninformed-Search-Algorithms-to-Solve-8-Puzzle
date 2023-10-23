from Algorithms.Algorithm_Factory import *


def main():
    notSolvable = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    test1 = [[8, 0, 6], [5, 4, 7], [2, 3, 1]]
    test2 = [[1, 2, 5], [3, 4, 0], [6, 7, 8]]
    test3 = [[1, 2, 5], [3, 4, 8], [6, 0, 7]]
    AStar_Manhattan = get_algorithm(test1, "BFS", "Manhattan")
    solution = AStar_Manhattan.solve()

    if solution.solvable:
        solution.print()


if __name__ == '__main__':
    main()
