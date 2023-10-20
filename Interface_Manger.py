import sys
sys.path.append('./Methods')
from Methods.Method_Manager import manager

def main():
    manhattan = manager([[1, 2, 5], [3, 4, 0], [6, 7, 8]], "Manhattan")
    solution = manhattan.solve()

    if solution.solvable:
        print(solution.cost, solution.nodes_expanded, solution.search_depth, solution.running_time, sep="\n")
        for state in solution.path:
            print(state)

if __name__ == '__main__':
    main()