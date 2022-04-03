'''
Puzzle.py merepresentasikan puzzle yang akan dicari solusinya.
'''
import copy
from Constant import SIZE

class Puzzle:
    '''
    constructor:
    '''
    def __init__(self, matrix):
        self.board = matrix

    '''
    membuat board dari 2d menjadi 1d
    '''
    def oneLineBoard(self):
        return [item for sublist in self.board for item in sublist]        
    
    '''
    mecari cell yang kosong
    return: tuple (row, col)
    '''
    def findEmpty(self):
        for i,row in enumerate(self.board):
            for j,value in enumerate(row):
                if(value==SIZE**2):
                    return (i,j)
    '''
    mengecek apakah empty cell berada di bagian arsir atau tidak
    return: 1 jika berada di bagian arsir 0 jika tidak
    '''
    def getParity(self):
        (r, c) = self.findEmpty()
        return (r+c) % 2

    '''
    memindahkan cell kosong ke (r+dr, c+dc)
    parameter:
        dr: row
        dc: column
    return: puzzle baru yang sudah dipindahkan
    '''
    def move(self, dr, dc):
        (r, c) = self.findEmpty()
        if(r+dr>=0 and r+dr<SIZE and c+dc>=0 and c+dc<SIZE):
            movedPuzzle = copy.deepcopy(self)
            movedPuzzle.board[r][c], movedPuzzle.board[r+dr][c+dc] = movedPuzzle.board[r+dr][c+dc], movedPuzzle.board[r][c]
            return movedPuzzle
        else:
            return None


    '''
    mengecek apakah puzzle solvable atau tidak
    return: True jika solvable, False jika tidak
    '''
    def solveable(self):
        flat = self.oneLineBoard()
        x = self.getParity()

        sum = 0
        for i in range(0,SIZE**2):
            var = 0
            for j in range(i+1,SIZE**2):
                if(flat[i]>flat[j]):
                    sum+=1
                    var+=1
            print("Kurang(",flat[i],") = ", var)
        print("Sigma Kurang(i):", sum)
        print("X:", x)
        print("Total:", sum + x, "(genap)" if (sum+x) % 2 == 0 else "(ganjil)")

        return (sum + x) % 2 == 0

    '''
    Mencetak Puzzle ke layar
    '''
    def printBoard(self):
        for row in self.board:
            for value in row:
                print('%4s' % (value if value!=SIZE**2 else "#"), end="")
            print()
        print("==================")

