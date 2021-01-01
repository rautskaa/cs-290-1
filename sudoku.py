class Sudoku:

    def __init__(self):
        """Initializes empty board, puzzle and continue game flag."""
        # Empty board
        self.empty_board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.continue_game_flag = True
        # Initial state of the puzzle
        self.generated_puzzle = [
            [0, 0, 0, 2, 6, 0, 7, 0, 1],
            [6, 8, 0, 0, 7, 0, 0, 9, 0],
            [1, 9, 0, 0, 0, 4, 5, 0, 0],
            [8, 2, 0, 1, 0, 0, 0, 4, 0],
            [0, 0, 4, 6, 0, 2, 9, 0, 0],
            [0, 5, 0, 0, 0, 3, 0, 2, 8],
            [0, 0, 9, 3, 0, 0, 0, 7, 4],
            [0, 4, 0, 0, 5, 0, 0, 3, 6],
            [7, 0, 3, 0, 1, 8, 0, 0, 0]]
        # Puzzle with default values
        self.generated_puzzle_default_values = [
            [0, 0, 0, 2, 6, 0, 7, 0, 1],
            [6, 8, 0, 0, 7, 0, 0, 9, 0],
            [1, 9, 0, 0, 0, 4, 5, 0, 0],
            [8, 2, 0, 1, 0, 0, 0, 4, 0],
            [0, 0, 4, 6, 0, 2, 9, 0, 0],
            [0, 5, 0, 0, 0, 3, 0, 2, 8],
            [0, 0, 9, 3, 0, 0, 0, 7, 4],
            [0, 4, 0, 0, 5, 0, 0, 3, 6],
            [7, 0, 3, 0, 1, 8, 0, 0, 0]]

    def get_board(self):
        """Returns puzzle board"""
        return self.generated_puzzle

    def get_default_values_board(self):
        """Returns default puzzle board"""
        return self.generated_puzzle_default_values

    def print_generated_puzzle(self):
        """Prints the puzzle"""
        for i in self.generated_puzzle:
            print(i)

    def print_board(self, given_board):
        """Prints the given puzzle"""
        for i in given_board:
            print(i)

    def get_continue_game_flag(self):
        """Returns continue game flag"""
        return self.continue_game_flag

    def set_continue_game_flag(self, result):
        """Sets continue game flag"""
        self.continue_game_flag = result

    def are_there_any_empty_cells_left(self):
        # Function to check whether there are still empty cells to fill
        board = self.get_board()
        for column in range(9):
            for row in range(9):
                if board[column][row] == 0:
                    return True

    def is_value_default(self, row, column):
        # Function to check whether user tries to change pre-defined value.
        default_board = self.get_default_values_board()
        if default_board[row][column] == 0:
            return True
        else:
            print("Pre-defined values cannot be changed.")
            return False

    def is_value_valid(self, row, column, value):
        # Function to check whether user entered values for row, column, value from 1 to 9.
        valid_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if row not in valid_numbers or column not in valid_numbers or value not in valid_numbers:
            return False
        return True