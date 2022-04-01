# puzzle.py
# Containing Puzzle class to represent states

import copy
from Constant import SIZE

class Puzzle:
    # Constructor
    def __init__(self, matrix):
        # Define board and size
        self.board = matrix
        print(self.board)

    # Find empty cell position
    # Returns : (row, colunn)
    def find_empty(self):
        for i,row in enumerate(self.board):
            for j,value in enumerate(row):
                if(value==SIZE**2):
                    return (i,j)

    # Move empty cell to (r+dr, c+dc)
    def move(self, dr, dc):
        (r, c) = self.find_empty()
        if(r+dr>=0 and r+dr<SIZE and c+dc>=0 and c+dc<SIZE):
            moved_puzzle = copy.deepcopy(self)
            moved_puzzle.board[r][c], moved_puzzle.board[r+dr][c+dc] = moved_puzzle.board[r+dr][c+dc], moved_puzzle.board[r][c]
            return moved_puzzle
        else:
            return None

    # Test whether the puzzle is solvable or not
    def is_solveable(self):
        # Get empty cell location
        (r, c) = self.find_empty()

        # Flatten board
        tmp = self.flattened_board()

        # Find empty cell parity
        x = (r+c) % 2

        sum = 0
        for i in range(0,SIZE**2):
            for j in range(i+1,SIZE**2):
                if(tmp[i]>tmp[j]):
                    sum+=1

        # Output value for verdict
        print("Inversions:", sum)
        print("Parity:", x)
        print("Total:", sum + x, "(even)" if (sum+x) % 2 == 0 else "(odd)")

        return (sum + x) % 2 == 0

    # Output board
    def output_board(self):
        for row in self.board:
            for value in row:
                print('%4s' % (value if value!=SIZE**2 else "#"), end="")
            print()
        print("----------------------------------------------------------------")

    # Return flattened board
    def flattened_board(self):
        return [val for arr in self.board for val in arr]
