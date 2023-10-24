# Import the necessary classes and modules
from Algorithms.Search_Algorithm import Search_Algorithm
from Algorithms.DFS import DFS
from Algorithms.BFS import BFS
from Algorithms.AStar import A_Star  # It seems there is a typo in the import

# Define a default goal test state and algorithm
DEFAULT_GOAL_TEST = 12345678
DEFAULT_ALGORITHM = "DFS"


# Function to get an instance of a search algorithm based on the input parameters
def get_algorithm(initial_state, algorithm, heuristic=None, goal_test=None):
    # If goal_test is not provided, use the default value
    if goal_test is None:
        goal_test = DEFAULT_GOAL_TEST

    # Use a match statement to determine the requested algorithm
    match algorithm:
        # If the requested algorithm is Depth-First Search (DFS), return a DFS instance
        case "DFS":
            return DFS(initial_state, goal_test)
        # If the requested algorithm is Breadth-First Search (BFS), return a BFS instance
        case "BFS":
            return BFS(initial_state, goal_test)
        # If the requested algorithm is A-Star, check if a heuristic is provided
        case "A-Star":
            if heuristic is None:
                return Search_Algorithm(initial_state, goal_test)
            # If a heuristic is provided, return an A-Star instance with the specified heuristic
            return A_Star(initial_state, goal_test, heuristic)
        # If the requested algorithm is not recognized, return a generic Search_Algorithm instance
        case _:
            return Search_Algorithm(initial_state, goal_test)
