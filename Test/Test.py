import unittest
from Algorithms.Algorithm_Factory import *


class Test(unittest.TestCase):
    algorithms = [
        ("A-Star", "Manhattan"),
        ("A-Star", "Euclidean"),
        ("DFS", None),
        ("BFS", None)
    ]

    def Solvable(self, initial_state):
        for algorithm, heuristic in self.algorithms:
            print(f"\n{algorithm}{' with ' + heuristic if heuristic else ''}:")
            puzzle = get_algorithm(initial_state, algorithm, heuristic)
            solution = puzzle.solve()
            print("Cost:", solution.stringify())
            self.assertTrue(solution.solvable)

    def notSolvable(self, initial_state, algorithm, heuristic=None):
        puzzle = get_algorithm(initial_state, algorithm, heuristic)
        solution = puzzle.solve()
        self.assertFalse(solution.solvable)

    def test_isSolvable(self):
        initial_states = [
            312045678,
            125340678,
            125348670,
            125348607,
            125308647,
            125038647,
            125638047,
            125638407,
            125638470,
            125630478,

            123406758,
            123456708,
            867254301,
            867254031,

            876543210,
            87654321,
            806547231,


            125340678,
            142658730,
            102754863
        ]

        for i, initial_state in enumerate(initial_states, 1):
            print(f'\n######## {i} ########')
            print(initial_state)
            self.Solvable(initial_state)

    def test_notSolvable(self):
        initial_states = [
            123456870,
            812043765,
            231054786,
            182453760
        ]
        for initial_state in initial_states:
            for algorithm, heuristic in self.algorithms:
                self.notSolvable(initial_state, algorithm, heuristic)

    def test_Manhattan1(self):
        puzzle = get_algorithm(125340678, "A-Star", "Manhattan")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 3)
        self.assertEqual(solution.nodes_expanded, 4)
        self.assertEqual(solution.search_depth, 3)

    def test_Manhattan2(self):
        puzzle = get_algorithm(142658730, "A-Star", "Manhattan")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 8)
        self.assertEqual(solution.nodes_expanded, 11)
        self.assertEqual(solution.search_depth, 8)

    def test_Manhattan3(self):
        puzzle = get_algorithm(125630478, "A-Star", "Manhattan")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 11)
        self.assertEqual(solution.nodes_expanded, 24)
        self.assertEqual(solution.search_depth, 11)

    def test_Euclidean1(self):
        puzzle = get_algorithm(125340678, "A-Star", "Euclidean")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 3)
        self.assertEqual(solution.nodes_expanded, 4)
        self.assertEqual(solution.search_depth, 3)

    def test_Euclidean2(self):
        puzzle = get_algorithm(142658730, "A-Star", "Euclidean")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 8)
        self.assertEqual(solution.nodes_expanded, 13)
        self.assertEqual(solution.search_depth, 8)

    def test_Euclidean3(self):
        puzzle = get_algorithm(125630478, "A-Star", "Euclidean")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 11)
        self.assertEqual(solution.nodes_expanded, 54)
        self.assertEqual(solution.search_depth, 11)

    def test_DFS1(self):
        puzzle = get_algorithm(312045678, "DFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 1)
        self.assertEqual(solution.nodes_expanded, 2)
        self.assertEqual(solution.search_depth, 1)

    def test_DFS2(self):
        puzzle = get_algorithm(125340678, "DFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 27)
        self.assertEqual(solution.nodes_expanded, 28)
        self.assertEqual(solution.search_depth, 27)

    def test_BFS1(self):
        puzzle = get_algorithm(312045678, "BFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 1)
        self.assertEqual(solution.nodes_expanded, 4)
        self.assertEqual(solution.search_depth, 2)

    def test_BFS2(self):
        puzzle = get_algorithm(125340678, "BFS")
        solution = puzzle.solve()
        self.assertTrue(solution.solvable)
        self.assertEqual(solution.cost, 3)
        self.assertEqual(solution.nodes_expanded, 13)
        self.assertEqual(solution.search_depth, 4)


if __name__ == '__main__':
    unittest.main()
