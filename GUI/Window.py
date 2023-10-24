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


def resize_image(photo_image, new_width, new_height):
    return photo_image.subsample(int(photo_image.width() / new_width), int(photo_image.height() / new_height))


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


class Window:
    def init_root(self):
        self.root.title("8-Puzzle")
        self.root.iconbitmap('GUI/Assets/icon.ico')
        self.root.resizable(False, False)
        self.root.configure(background=BACKGROUND_COLOR)

    def init_styles(self):
        self.style.configure("Custom.TFrame", background=BACKGROUND_COLOR, font=("Helvetica", 14))
        self.style.configure("Custom.TCombobox", lightcolor=FOCUSED_COLOR)
        self.style.configure("Custom.TEntry", highlightcolor=FOCUSED_COLOR)
        self.style.configure("Custom.TButton", background=BACKGROUND_COLOR, color=BOARD_COLOR)
        self.style.configure("Custom.TLabel", background=BACKGROUND_COLOR, foreground="white", font=("Helvetica", 14))
        self.style.configure("Solution.TLabel", background=BACKGROUND_COLOR, foreground="white", font=("Helvetica", 11))

    def init_algorithm_view(self):
        self.algorithm_label = ttk.Label(self.side_frame, text="Select Algorithm:", style="Custom.TLabel")
        self.algorithm_label.pack(pady=(8, 4))
        self.algorithm_var = tk.StringVar()
        self.algorithm_combobox = ttk.Combobox(self.side_frame, textvariable=self.algorithm_var,
                                               values=["DFS", "BFS", "A-Star (Manhattan)", "A-Star (Euclidean)"],
                                               state="readonly", style="Custom.TCombobox")
        self.algorithm_combobox.current(0)
        self.algorithm_combobox.pack(pady=(0, 16))

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

    def init_solution_view(self):
        self.solution_header_label = ttk.Label(self.side_frame, style="Custom.TLabel")
        self.solution_body_label = ttk.Label(self.side_frame, style="Solution.TLabel")
        self.solution_header_label.pack(pady=(30, 8), padx=0)
        self.solution_body_label.pack(padx=0)

    def init_canvas_view(self):
        self.canvas = tk.Canvas(self.root, width=BOARD_GUI_DIMENSION, height=BOARD_GUI_DIMENSION,
                                highlightbackground=BACKGROUND_COLOR)
        self.canvas.pack()

    def __init__(self):
        # initialize the window
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

    def load_images(self):
        self.tile_images = []
        for i in range(1, 9):
            tile_image = tk.PhotoImage(file=f"GUI/Assets/{i}.png")
            tile_image = resize_image(tile_image, BOARD_GUI_DIMENSION / BOARD_DIMENSION, BOARD_GUI_DIMENSION / BOARD_DIMENSION)
            self.tile_images.append(tile_image)
        self.draw_board(convert_int_to_state(DEFAULT_INITIAL_STATE))

    def display_next_state(self):
        self.previous_state_button.configure(state="normal")
        self.draw_board(self.states[self.current_state_index + 1])
        self.current_state_index += 1
        self.current_state_label.configure(text="Current State: " + str(self.current_state_index))
        if self.current_state_index + 1 >= len(self.states):
            self.next_state_button.configure(state="disabled")

    def display_previous_state(self):
        self.next_state_button.configure(state="normal")
        self.draw_board(self.states[self.current_state_index - 1])
        self.current_state_index -= 1
        self.current_state_label.configure(text="Current State: " + str(self.current_state_index))
        if self.current_state_index - 1 < 0:
            self.previous_state_button.configure(state="disabled")

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

        # taking the method
        algorithm = self.algorithm_var.get()
        heuristic = None

        if algorithm[:6] == "A-Star":
            heuristic = algorithm[7:]
            algorithm = algorithm[:6]
            heuristic = heuristic[1:-1]

        # solving the board
        algorithm = get_algorithm(initial_state, algorithm, heuristic, goal_test)
        solution = algorithm.solve()

        # checking if the board has a solution
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
