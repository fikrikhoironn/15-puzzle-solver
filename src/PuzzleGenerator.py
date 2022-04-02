from Constant import SIZE
import numpy as np

'''
membuat matrix puzzle random berukuran 4 x 4 berisi angka 1-16 secara acak
'''
class PuzzleGenerator:
    def __init__(self):
        self.matrix = []
        temp = np.random.permutation(np.arange(1, 17))
        temp = np.ndarray.tolist(temp)
        self.matrix.append(temp[0:4])
        self.matrix.append(temp[4:8])
        self.matrix.append(temp[8:12])
        self.matrix.append(temp[12:16])
    
    '''
    mengambil matrix puzzle
    return: matrix puzzle
    '''
    def getMatrix(self):
        return self.matrix
