import unittest
from Algorithms.Algorithm_Factory import *


class Test(unittest.TestCase):
    algorithms = [
        ("AStar", "Manhattan"),
        ("AStar", "Euclidean"),
        ("DFS", None),
        ("BFS", None)
    ]

    def Solvable(self, initial_state):
        for algorithm, heuristic in self.algorithms:
            print(f"\n{algorithm}{' with ' + heuristic if heuristic else ''}:")
            puzzle = get_algorithm(initial_state, algorithm, heuristic)
            solution = puzzle.solve()
            print("Cost:", solution.cost)
            print("Nodes expanded:", solution.nodes_expanded)
            print("Search depth:", solution.search_depth)
            print("Running time:", solution.running_time, "Sec")
            self.assertTrue(solution.solvable)

    def notSolvable(self, initial_state, algorithm, heuristic=None):
        puzzle = get_algorithm(initial_state, algorithm, heuristic)
        solution = puzzle.solve()
        self.assertFalse(solution.solvable)

    def test_isSolvable(self):
        initial_states = [
            [[3, 1, 2], [0, 4, 5], [6, 7, 8]],
            [[1, 2, 5], [3, 4, 0], [6, 7, 8]],
            [[1, 2, 5], [3, 4, 8], [6, 7, 0]],
            [[1, 2, 5], [3, 4, 8], [6, 0, 7]],
            [[1, 2, 5], [3, 0, 8], [6, 4, 7]],
            [[1, 2, 5], [0, 3, 8], [6, 4, 7]],
            [[1, 2, 5], [6, 3, 8], [0, 4, 7]],
            [[1, 2, 5], [6, 3, 8], [4, 0, 7]],
            [[1, 2, 5], [6, 3, 8], [4, 7, 0]],
            [[1, 2, 5], [6, 3, 0], [4, 7, 8]],

            [[1, 2, 3], [4, 0, 6], [7, 5, 8]],
            [[1, 2, 3], [4, 5, 6], [7, 0, 8]],
            [[8, 6, 7], [2, 5, 4], [3, 0, 1]],
            [[8, 6, 7], [2, 5, 4], [0, 3, 1]],

            [[8, 7, 6], [5, 4, 3], [2, 1, 0]],
            [[0, 8, 7], [6, 5, 4], [3, 2, 1]],
            [[8, 0, 6], [5, 4, 7], [2, 3, 1]],

            [[1, 2, 5], [3, 4, 0], [6, 7, 8]],
            [[1, 4, 2], [6, 5, 8], [7, 3, 0]],
            [[1, 0, 2], [7, 5, 4], [8, 6, 3]],
        ]

        for i, initial_state in enumerate(initial_states, 1):
            print(f'\n######## {i} ########')
            self.Solvable(initial_state)

    def test_notSolvable(self):
        initial_states = [
            [[1, 2, 3], [4, 5, 6], [8, 7, 0]],
            [[8, 1, 2], [0, 4, 3], [7, 6, 5]],
            [[2, 3, 1], [0, 5, 4], [7, 8, 6]],
            [[1, 8, 2], [4, 5, 3], [7, 6, 0]],
        ]
        for initial_state in initial_states:
            for algorithm, heuristic in self.algorithms:
                self.notSolvable(initial_state, algorithm, heuristic)

    def test_Manhattan1(self):
        puzzle = get_algorithm([[1, 2, 5], [3, 4, 0], [6, 7, 8]], "AStar", "Manhattan")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 3)
        self.assertEqual(solution.nodes_expanded, 4)
        self.assertEqual(solution.search_depth, 3)

    def test_Manhattan2(self):
        puzzle = get_algorithm([[1, 4, 2], [6, 5, 8], [7, 3, 0]], "AStar", "Manhattan")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 8)
        self.assertEqual(solution.nodes_expanded, 11)
        self.assertEqual(solution.search_depth, 8)

    def test_Manhattan3(self):
        puzzle = get_algorithm([[1, 2, 5], [6, 3, 0], [4, 7, 8]], "AStar", "Manhattan")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 11)
        self.assertEqual(solution.nodes_expanded, 24)
        self.assertEqual(solution.search_depth, 11)

    def test_Euclidean1(self):
        puzzle = get_algorithm([[1, 2, 5], [3, 4, 0], [6, 7, 8]], "AStar", "Euclidean")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 3)
        self.assertEqual(solution.nodes_expanded, 4)
        self.assertEqual(solution.search_depth, 3)

    def test_Euclidean2(self):
        puzzle = get_algorithm([[1, 4, 2], [6, 5, 8], [7, 3, 0]], "AStar", "Euclidean")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 8)
        self.assertEqual(solution.nodes_expanded, 13)
        self.assertEqual(solution.search_depth, 8)

    def test_Euclidean3(self):
        puzzle = get_algorithm([[1, 2, 5], [6, 3, 0], [4, 7, 8]], "AStar", "Euclidean")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 11)
        self.assertEqual(solution.nodes_expanded, 54)
        self.assertEqual(solution.search_depth, 11)

    def test_DFS1(self):
        puzzle = get_algorithm([[3, 1, 2], [0, 4, 5], [6, 7, 8]], "DFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 1)
        self.assertEqual(solution.nodes_expanded, 2)
        self.assertEqual(solution.search_depth, 1)

    def test_DFS2(self):
        puzzle = get_algorithm(  [[1, 2, 5], [3, 4, 0], [6, 7, 8]], "DFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 27)
        self.assertEqual(solution.nodes_expanded, 28)
        self.assertEqual(solution.search_depth, 27)

    def test_BFS1(self):
        puzzle = get_algorithm([[3, 1, 2], [0, 4, 5], [6, 7, 8]], "BFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 1)
        self.assertEqual(solution.nodes_expanded, 4)
        self.assertEqual(solution.search_depth, 2)

    def test_BFS2(self):
        puzzle = get_algorithm([[1, 2, 5], [3, 4, 0], [6, 7, 8]], "BFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 3)
        self.assertEqual(solution.nodes_expanded, 13)
        self.assertEqual(solution.search_depth, 4)


if __name__ == '__main__':
    unittest.main()
