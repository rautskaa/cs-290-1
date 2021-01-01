# Course: CS325 - Analysis of Algorithms
# Student Name: Aksana Rautskaya
# Assignment: Portfolio project
# Description: Implements sudoku puzzle: the game and verification. It supports the following features: user can play
# the sudoku game and then user's solution can be verified on correctness.

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

    def check_for_quit_game(self, user_input):
        # Function to check whether user wants to exit the game.
        if user_input == "q" or user_input == "Q":
            exit()

    def verify_solution_user_choice(self, user_input):
        # Function to check whether user is ready to verify the game.
        if user_input == "v" or user_input == "V":
            self.set_continue_game_flag(False)
            self.verify_solution()

    def verify_solution(self):
        """Function to verify user's solution."""
        board = self.get_board()
        existing_numbers = []
        # verify whether board has any empty cells, if so, solution is not valid
        for column in range(9):
            for row in range(9):
                if board[column][row] == 0:
                    print("Solution is not valid. Board has at least one empty cell")
                    return False
        # verify each row for correctness of the solution, if a number is duplicated in a row, return False
        for row in range(9):
            for cell in range(9):
                if board[row][cell] not in existing_numbers:
                    existing_numbers.append(board[row][cell])
                else:
                    print("Solution is not valid. Board has duplicate value in at least one row")
                    return False
            existing_numbers = []
        # verify each column for correctness of the solution, if a number is duplicated in a column, return False
        existing_numbers = []
        for column in range(9):
            for cell in range(9):
                if board[cell][column] not in existing_numbers:
                    existing_numbers.append(board[cell][column])
                else:
                    print("Solution is not valid. Board has duplicate value in at least one column")
                    return False
            existing_numbers = []
        # verify each subgrid for correctness of the solution, if a number is duplicated in a subgrid, return False
        # Check all nine subgrids
        for number in range(9):
            existing_numbers = []
            # subgrid #1
            if number == 0:
                column = 1
                row = 1
            # subgrid #2
            if number == 1:
                column = 4
                row = 1
            # subgrid #3
            if number == 2:
                column = 7
                row = 1
            # subgrid #4
            if number == 3:
                column = 1
                row = 4
            # subgrid #5
            if number == 4:
                column = 4
                row = 4
            # subgrid #6
            if number == 5:
                column = 7
                row = 4
            # subgrid #7
            if number == 6:
                column = 1
                row = 7
            # subgrid #8
            if number == 7:
                column = 4
                row = 7
            # subgrid #9
            if number == 8:
                column = 7
                row = 7
            if board[column][row] not in existing_numbers:
                existing_numbers.append(board[column][row])
            else:
                print("Solution is not valid. Board has duplicate value in at least one subgrid")
                return False
            if board[column-1][row] not in existing_numbers:
                existing_numbers.append(board[column-1][row])
            else:
                print("Solution is not valid. Board has duplicate value in at least one subgrid")
                return False
            if board[column+1][row] not in existing_numbers:
                existing_numbers.append(board[column+1][row])
            else:
                print("Solution is not valid. Board has duplicate value in at least one subgrid")
                return False
            if board[column][row-1] not in existing_numbers:
                existing_numbers.append(board[column][row-1])
            else:
                print("Solution is not valid. Board has duplicate value in at least one subgrid")
                return False
            if board[column-1][row-1] not in existing_numbers:
                existing_numbers.append(board[column-1][row-1])
            else:
                print("Solution is not valid. Board has duplicate value in at least one subgrid")
                return False
            if board[column+1][row-1] not in existing_numbers:
                existing_numbers.append(board[column+1][row-1])
            else:
                print("Solution is not valid. Board has duplicate value in at least one subgrid")
                return False
            if board[column-1][row+1] not in existing_numbers:
                existing_numbers.append(board[column-1][row+1])
            else:
                print("Solution is not valid. Board has duplicate value in at least one subgrid")
                return False
            if board[column+1][row+1] not in existing_numbers:
                existing_numbers.append(board[column+1][row+1])
            else:
                print("Solution is not valid. Board has duplicate value in at least one subgrid")
                return False
            if board[column][row+1] not in existing_numbers:
                existing_numbers.append(board[column][row+1])
            else:
                print("Solution is not valid. Board has duplicate value in at least one subgrid")
                return False
        print("Solution is valid")
        return True

    def start_sudoku_game(self):
        """The main function that start sudoku game"""
        continue_flag = self.get_continue_game_flag()
        # As long as there is at least one empty cell, ask user to fill in cells
        while self.get_continue_game_flag():
            self.play_sudoku()

    def play_sudoku(self):
        """Function that takes user input and modified the board accordingly."""
        board = self.get_board()
        if not self.are_there_any_empty_cells_left():
            user_value = input(
                "All cells are filled! Enter v to verify your solution or enter 3 new numbers from 1 to 9 for column, "
                "row and value separated by space (ex. 5 1 3). ""Enter q to ""exit the game ")
        else:
            user_value = input("Enter 3 numbers from 1 to 9 for column, row and value separated by space (ex. 5 1 3). "
                                    "Enter q to ""exit the game ")
        print()
        new_user_input = []
        # Check if user wants to quit game
        self.check_for_quit_game(user_value)
        # Check if user wants to verify solution
        self.verify_solution_user_choice(user_value)
        if not self.get_continue_game_flag():
            return
        user_value = user_value.split()
        # Make sure user entered values in correct format
        if len(user_value) != 3:
            print("Entered format is incorrect. Let's try again")
            self.play_sudoku()
            return
        # Make sure user entered number is digit
        for n in user_value:
            if not n.isdigit():
                print("At least one of the entered characters is not a number. Let's try again")
                self.play_sudoku()
                return
        # Add string values to int array
        for n in user_value:
            new_user_input.append(int(n))
        # Assign each value to column, row, value
        column = new_user_input[0]
        row = new_user_input[1]
        value = new_user_input[2]
        # Check if user entered values between 1 to 9
        if not self.is_value_valid(row, column, value):
            print("Entered values should be numbers from 1 to 9. Let's try again")
            self.play_sudoku()
        # If user's entered values are trying to change default values, ask user to enter a new value
        if not self.is_value_default(row - 1, column - 1):
            self.play_sudoku()
        # Update the board with the chosen value
        else:
            board[row - 1][column - 1] = value
            self.print_board(board)
            print()
            print("Successfully added " + str(value) + " to " + "column #" + str(column) + " row #" + str(row))

game = Sudoku()
print()
print("Here is Sudoku puzzle for you to solve:")
print()
game.print_board(game.generated_puzzle)
print()
game.start_sudoku_game()