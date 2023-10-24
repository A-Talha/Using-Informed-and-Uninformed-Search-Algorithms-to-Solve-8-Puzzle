import tkinter as tk
from tkinter import ttk

from Algorithms.Algorithm_Factory import get_algorithm

BOARD_DIMENSION = 3
BOARD_GUI_DIMENSION = 584
DEFAULT_INITIAL_STATE = 12345678
BOARD_COLOR = "#202020"
FOCUSED_COLOR = "#ebb735"
BACKGROUND_COLOR = "#404040"
TRANSPARENT_COLOR = "#00000088"


# Function to resize an image.
def resize_image(photo_image, new_width, new_height):
    return photo_image.subsample(int(photo_image.width() / new_width), int(photo_image.height() / new_height))


# Function to validate user input for the puzzle state.
def validate_input(state):
    try:
        state = state.replace(',', '')
        unique_chars = set()
        for i in range(len(state)):
            if state[i] in unique_chars:
                return None
            unique_chars.add(state[i])
        if len(unique_chars) < 8 or len(unique_chars) > 9:
            return None
        state = int(state)
        return state
    except ValueError:
        return None


# Function to convert an integer state into a 2D board representation.
def convert_int_to_state(state):
    state_str = str(state)
    if len(state_str) == 8:
        state_str = '0' + state_str

    state_board = []
    for i in range(BOARD_DIMENSION):
        row = []
        for j in range(BOARD_DIMENSION):
            row.append(int(state_str[i * BOARD_DIMENSION + j]))
        state_board.append(row)
    return state_board


# Function to get the coordinates of the empty tile in a state.
def get_empty_tile(state):
    return next(((x, y) for x, row in enumerate(state) for y, val in enumerate(row) if val == 0))


# Function to get the move required to go from one state to another.
def get_move(from_state, to_state):
    from_x, from_y = get_empty_tile(to_state)
    to_x, to_y = get_empty_tile(from_state)
    return from_x, from_y, to_x, to_y


# Class to manage the GUI window.
class Window:
    def __init__(self):
        # Initialize the window and set up its components.
        self.animating_tile = False
        self.states = None
        self.side_frame = None
        self.algorithm_label = None
        self.algorithm_var = None
        self.algorithm_combobox = None
        self.tile_images = None
        self.initial_state_label = None
        self.state_description_label = None
        self.initial_state_entry = None
        self.goal_test_label = None
        self.default_goal_label = None
        self.goal_test_entry = None
        self.solve_button = None
        self.buttons_frame = None
        self.next_state_button = None
        self.previous_state_button = None
        self.current_state_label = None
        self.solution_header_label = None
        self.solution_body_label = None
        self.canvas = None
        self.root = tk.Tk()
        self.style = ttk.Style()

        self.init_root()
        self.init_styles()

        self.side_frame = ttk.Frame(self.root, style="Custom.TFrame")
        self.side_frame.pack(side=tk.LEFT, padx=16, pady=10, expand=True, fill="both")

        self.init_algorithm_view()
        self.init_initial_state_view()
        self.init_goal_test_view()
        self.init_navigation_view()
        self.init_solution_view()
        self.init_canvas_view()

        self.load_images()
        self.current_state_index = 0

        self.root.mainloop()

    # Function to initialize the root window.
    def init_root(self):
        self.root.title("8-Puzzle")
        self.root.iconbitmap('GUI/Assets/icon.ico')
        self.root.resizable(False, False)
        self.root.configure(background=BACKGROUND_COLOR)

    # Function to set up the visual styles for GUI elements.
    def init_styles(self):
        self.style.configure("Custom.TFrame", background=BACKGROUND_COLOR, font=("Helvetica", 14))
        self.style.configure("Custom.TCombobox", lightcolor=FOCUSED_COLOR)
        self.style.configure("Custom.TEntry", highlightcolor=FOCUSED_COLOR)
        self.style.configure("Custom.TButton", background=BACKGROUND_COLOR, color=BOARD_COLOR)
        self.style.configure("Custom.TLabel", background=BACKGROUND_COLOR, foreground="white", font=("Helvetica", 14))
        self.style.configure("Solution.TLabel", background=BACKGROUND_COLOR, foreground="white", font=("Helvetica", 11))

    # Function to initialize the algorithm selection view.
    def init_algorithm_view(self):
        self.algorithm_label = ttk.Label(self.side_frame, text="Select Algorithm:", style="Custom.TLabel")
        self.algorithm_label.pack(pady=(8, 4))
        self.algorithm_var = tk.StringVar()
        self.algorithm_combobox = ttk.Combobox(self.side_frame, textvariable=self.algorithm_var,
                                               values=["DFS", "BFS", "A-Star (Manhattan)", "A-Star (Euclidean)"],
                                               state="readonly", style="Custom.TCombobox")
        self.algorithm_combobox.current(0)
        self.algorithm_combobox.pack(pady=(0, 16))

    # Function to initialize the initial state input view.
    def init_initial_state_view(self):
        self.initial_state_label = ttk.Label(self.side_frame, text="Enter Initial State:", style="Custom.TLabel")
        self.initial_state_label.pack(pady=(8, 2))
        self.state_description_label = ttk.Label(self.side_frame,
                                                 text="Write state in this form\n      0,2,1,3,8,6,5,4,7",
                                                 background=BACKGROUND_COLOR, foreground="white",
                                                 font=("Helvetica", 11))
        self.state_description_label.pack(pady=(0, 4))
        self.initial_state_entry = ttk.Entry(self.side_frame, style="Custom.TEntry")
        self.initial_state_entry.pack(pady=(0, 8))

    # Function to initialize the goal state input view.
    def init_goal_test_view(self):
        self.goal_test_label = ttk.Label(self.side_frame, text="Enter Goal State:", style="Custom.TLabel")
        self.goal_test_label.pack(pady=(8, 2))
        self.default_goal_label = ttk.Label(self.side_frame,
                                            text="If left empty goal state is\n      0,1,2,3,4,5,6,7,8",
                                            background=BACKGROUND_COLOR, foreground="white",
                                            font=("Helvetica", 11))
        self.default_goal_label.pack(pady=(0, 4))
        self.goal_test_entry = ttk.Entry(self.side_frame, style="Custom.TEntry")
        self.goal_test_entry.pack(pady=(0, 8))

    # Function to initialize the navigation and solution views.
    def init_navigation_view(self):
        self.solve_button = ttk.Button(self.side_frame, text="Solve", style="Custom.TButton",
                                       command=lambda: self.get_solution())
        self.buttons_frame = ttk.Frame(self.side_frame, style="Custom.TFrame")
        self.next_state_button = ttk.Button(self.buttons_frame, text="Next", command=lambda: self.display_next_state(),
                                            style="Custom.TButton")
        self.previous_state_button = ttk.Button(self.buttons_frame, text="Previous",
                                                command=lambda: self.display_previous_state(),
                                                style="Custom.TButton")
        self.previous_state_button.grid(row=0, column=0, padx=(3, 6))
        self.next_state_button.grid(row=0, column=1, padx=(6, 3))

        self.current_state_label = ttk.Label(self.side_frame, text="", style="Solution.TLabel")

        self.previous_state_button.configure(state="disabled")
        self.next_state_button.configure(state="disabled")

        self.solve_button.pack(pady=(0, 36))
        self.buttons_frame.pack(pady=(0, 4))
        self.current_state_label.pack(pady=(8, 2))

    # Function to initialize the solution view.
    def init_solution_view(self):
        self.solution_header_label = ttk.Label(self.side_frame, style="Custom.TLabel")
        self.solution_body_label = ttk.Label(self.side_frame, style="Solution.TLabel")
        self.solution_header_label.pack(pady=(30, 8), padx=0)
        self.solution_body_label.pack(padx=0)

    # Function to initialize the puzzle board canvas view.
    def init_canvas_view(self):
        self.canvas = tk.Canvas(self.root, width=BOARD_GUI_DIMENSION, height=BOARD_GUI_DIMENSION,
                                highlightbackground=BACKGROUND_COLOR)
        self.canvas.pack()

    # Function to load tile images for the puzzle.
    def load_images(self):
        self.tile_images = []
        for i in range(1, 9):
            tile_image = tk.PhotoImage(file=f"GUI/Assets/{i}.png")
            tile_image = resize_image(tile_image, BOARD_GUI_DIMENSION / BOARD_DIMENSION,
                                      BOARD_GUI_DIMENSION / BOARD_DIMENSION)
            self.tile_images.append(tile_image)
        self.draw_board(convert_int_to_state(DEFAULT_INITIAL_STATE))

    # Function to display the next state in the solution sequence.
    def display_next_state(self):
        if self.animating_tile:
            return
        self.previous_state_button.configure(state="normal")
        self.animate_tile_movement(self.states[self.current_state_index], self.states[self.current_state_index + 1])
        self.current_state_index += 1
        self.current_state_label.configure(text="Current State: " + str(self.current_state_index))
        if self.current_state_index + 1 >= len(self.states):
            self.next_state_button.configure(state="disabled")

    # Function to display the previous state in the solution sequence.
    def display_previous_state(self):
        if self.animating_tile:
            return
        self.next_state_button.configure(state="normal")
        self.animate_tile_movement(self.states[self.current_state_index], self.states[self.current_state_index - 1])
        self.current_state_index -= 1
        self.current_state_label.configure(text="Current State: " + str(self.current_state_index))
        if self.current_state_index - 1 < 0:
            self.previous_state_button.configure(state="disabled")

    def animate_tile_movement(self, from_state, to_state):
        # Set the flag to indicate that an animation is in progress
        self.animating_tile = True

        # Calculate the dimensions of each cell in the board
        cell_width = BOARD_GUI_DIMENSION / BOARD_DIMENSION
        cell_height = BOARD_GUI_DIMENSION / BOARD_DIMENSION

        # Get the coordinates of the empty tile in the from and to states
        from_x, from_y, to_x, to_y = get_move(from_state, to_state)

        # Calculate the movement steps.
        dx = (to_x - from_x) * cell_width / 10
        dy = (to_y - from_y) * cell_height / 10

        # Perform the animation using the `after` method.
        def move_tile(step=1):
            if step <= 10:
                # Move the tile by dx and dy
                self.canvas.delete("all")
                for i in range(BOARD_DIMENSION):
                    for j in range(BOARD_DIMENSION):
                        value = from_state[i][j]
                        if i == from_x and j == from_y:
                            self.canvas.create_image(j * cell_width + dy * step, i * cell_height + dx * step,
                                                     anchor=tk.NW, image=self.tile_images[value - 1])
                        elif value != 0:
                            self.canvas.create_image(j * cell_width, i * cell_height, anchor=tk.NW,
                                                     image=self.tile_images[value - 1])
                self.root.after(15, move_tile, step + 1)
            else:
                # Set the flag to indicate that the animation is complete
                self.animating_tile = False

        move_tile()
            
    # Function to draw the puzzle board on the canvas.
    def draw_board(self, state):
        self.canvas.delete("all")
        cell_width = BOARD_GUI_DIMENSION / BOARD_DIMENSION
        cell_height = BOARD_GUI_DIMENSION / BOARD_DIMENSION

        for i in range(BOARD_DIMENSION):
            for j in range(BOARD_DIMENSION):
                value = state[i][j]
                if value != 0:
                    self.canvas.create_image(j * cell_width, i * cell_height, anchor=tk.NW,
                                             image=self.tile_images[value - 1])

    # Function to get the solution to the puzzle.
    def get_solution(self):
        self.current_state_index = 0
        self.previous_state_button.configure(state="disabled")
        self.next_state_button.configure(state="disabled")

        initial_state = self.initial_state_entry.get()
        goal_test = self.goal_test_entry.get()
        initial_state = validate_input(initial_state)
        goal_test = validate_input(goal_test)

        if initial_state is None:
            self.current_state_label.configure(text="", style="Solution.TLabel")
            self.solution_header_label.configure(text="Invalid Initial State!")
            self.solution_body_label.configure(text="")
            return

        # Get the selected algorithm and heuristic.
        algorithm = self.algorithm_var.get()
        heuristic = None

        if algorithm[:6] == "A-Star":
            heuristic = algorithm[7:]
            algorithm = algorithm[:6]
            heuristic = heuristic[1:-1]

        # Solve the puzzle with the selected algorithm.
        algorithm = get_algorithm(initial_state, algorithm, heuristic, goal_test)
        solution = algorithm.solve()

        # Check if the puzzle has a solution.
        if solution.solvable:
            self.current_state_label.configure(text="Current State: " + str(self.current_state_index))
            self.solution_header_label.configure(text="Solution exists!")
            self.solution_body_label.configure(text=solution.stringify())

            self.states = solution.path
            if len(self.states) > 1:
                self.next_state_button.configure(state="enabled")
            self.states = list(map(lambda state: convert_int_to_state(state), self.states))
            self.draw_board(self.states[0])
        else:
            self.current_state_label.configure(text="", style="Solution.TLabel")
            self.solution_header_label.configure(text="No Solution :(")
            self.solution_body_label.configure(text="")
            self.draw_board(convert_int_to_state(initial_state))

        self.root.update()
