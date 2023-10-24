# Define the board dimension (assuming it's a 3x3 board)
BOARD_DIMENSION = 3


# Function to calculate the Manhattan distance between two points
def manhattan_distance(x1, y1, x2, y2):
    # Calculate the absolute difference in x and y coordinates and sum them to get the Manhattan distance
    return abs(x1 - x2) + abs(y1 - y2)


# Heuristic function that calculates the Manhattan heuristic for a given state
def manhattan_heuristic(state, goal_state):
    # Initialize the sum of Manhattan distances to 0
    manhattan_sum = 0
    # Calculate the total number of cells on the board (assuming it's a 3x3 board)
    board_size = BOARD_DIMENSION * BOARD_DIMENSION

    # Create a dictionary to store the current location of each tile
    current_location = dict()
    state_int = goal_state
    for i in range(board_size):
        current_location[state_int % 10] = board_size - 1 - i
        state_int //= 10

    # Iterate through each cell of the state
    for i in range(board_size):
        # Extract the value in the current cell (rightmost digit)
        val = state % 10

        # Check if the value is not 0 (not an empty cell)
        if val:
            # Calculate the Manhattan distance from the current cell position to its goal position
            # (board_size - 1 - i) // BOARD_DIMENSION gives the goal row, and (board_size - 1 - i) % BOARD_DIMENSION gives the goal column
            manhattan_sum += manhattan_distance((board_size - 1 - i) // BOARD_DIMENSION,
                                                (board_size - 1 - i) % BOARD_DIMENSION, current_location[val] // BOARD_DIMENSION,
                                                current_location[val] % BOARD_DIMENSION)

        # Remove the rightmost digit to process the next cell
        state //= 10

    # Return the sum of Manhattan distances as the heuristic value
    return manhattan_sum
