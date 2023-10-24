# Import the square root function from the math module
from math import sqrt

# Define the board dimension (assuming it's a 3x3 board)
BOARD_DIMENSION = 3


# Function to calculate the Euclidean distance between two points
def euclidean_distance(x1, y1, x2, y2):
    # Use the Pythagorean theorem to calculate the Euclidean distance
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Heuristic function that calculates the Euclidean heuristic for a given state
def euclidean_heuristic(state):
    # Initialize the sum of Euclidean distances to 0
    euclidean_sum = 0
    # Calculate the total number of cells on the board (assuming it's a 3x3 board)
    board_size = BOARD_DIMENSION * BOARD_DIMENSION

    # Iterate through each cell of the state
    for i in range(board_size):
        # Extract the value in the current cell (rightmost digit)
        val = state % 10

        # Calculate the Euclidean distance from the current cell position to its goal position
        # (board_size - 1 - i) // BOARD_DIMENSION gives the goal row, and (board_size - 1 - i) % BOARD_DIMENSION gives the goal column
        euclidean_sum += euclidean_distance((board_size - 1 - i) // BOARD_DIMENSION, (board_size - 1 - i) % BOARD_DIMENSION, val // BOARD_DIMENSION, val % BOARD_DIMENSION)

        # Remove the rightmost digit to process the next cell
        state //= 10

    # Return the sum of Euclidean distances as the heuristic value
    return euclidean_sum
