'''
Node digunakan untuk merepresentasikan pohon ruang status dalam branch and bound
'''
class Node:
    def __init__(self, root, parent = None, depth=0, move=""):
        self.root = root
        self.parent = parent
        self.move = move
        self.depth = depth
