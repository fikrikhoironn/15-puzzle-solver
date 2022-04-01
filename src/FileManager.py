
class FileManager:
    def __init__(self, path):
        # self.board = []
        # f = open(path, "r")
        # for line in f:
        #     self.board.append(list(map(lambda x : int(x), line.split())))
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

            
    def get_board(self):
        # return self.board
        return self.matrix