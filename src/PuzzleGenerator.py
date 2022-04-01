# create random matrix 4 x 4
from Constant import SIZE
import numpy as np
# random matrix 4 x 4

class PuzzleGenerator:
    def __init__(self):
        self.matriks = []
        temp = np.random.permutation(np.arange(1, 17))
        temp = np.ndarray.tolist(temp)
        self.matriks.append(temp[0:4])
        self.matriks.append(temp[4:8])
        self.matriks.append(temp[8:12])
        self.matriks.append(temp[12:16])
    
    def get_board(self):
        return self.matriks
