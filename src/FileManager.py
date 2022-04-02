class FileManager:
    '''
    membuat matrix puzzle dari file 
    '''
    def __init__(self, path):
        f = open(path, "r")
        temp = f.readlines()
        self.matrix = []
        for item in temp:
            a = item.strip("\n").split(" ")
            self.matrix.append(a)
        for i in range(4) :
            for j in range(4) :
                if self.matrix[i][j] == 'X' :
                    self.matrix[i][j] = 16
                else :
                    self.matrix[i][j] = int(self.matrix[i][j])

    '''
    mengambil matrix puzzle
    return: matrix puzzle
    '''        
    def getMatrix(self):
        return self.matrix