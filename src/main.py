# main.py
# Contains main program and several functions for aiding Branch and Bound

from Puzzle import Puzzle
from FileManager import FileManager
from PriorityQueue import PriorityQueue
from Node import Node
from Constant import SIZE
from PuzzleGenerator import PuzzleGenerator
import time


'''
megecek apakah puzzle sudah terurut
parameter:
    puzzle: puzzle yang akan dicek
return:
    True jika puzzle sudah terurut
'''
def isFinish(puzzle):
    flat = puzzle.oneLineBoard()
    for i in range(1, (SIZE**2)+1):
        if(flat[i-1] != i):
            return False

    return True

'''
mencetak puzzle solusi langkah yang diambil sampai ke solusi akhir
'''
def generateSolution(solved_state):
    Node_solution = []

    parent = solved_state.parent
    state = solved_state

    while(parent != None):
       Node_solution.insert(0, state) 
       state = parent
       parent = parent.parent
    for i in range(len(Node_solution)):
        Node_solution[i].root.printBoard()
    return Node_solution

'''
mengecek banyak tiles yang tidak sesuai dengan posisinya
parameter:
    puzzle: puzzle yang akan dicek
return:
    banyak tiles yang tidak sesuai dengan posisinya
'''
def numberMisplacedTiles(puzzle):
    result = 0
    flat = puzzle.oneLineBoard()
    
    for i in range(1, SIZE**2+1):
        if(flat[i-1] != i):
            result+=1

    return result


def main():
    '''
    Tahap Input
    '''
    choose = int(input("1. Random puzzle\n2. Input puzzle (direkomendasikan)\n"))
    if (choose == 1):
        file = PuzzleGenerator()
        root = Node(Puzzle(file.getMatrix()))
    elif(choose == 2):
        filename = input("Masukkan nama file puzzle: contoh: solveable_01.txt\n")
        try:
            fm = FileManager("../test/" + filename)
            root = Node(Puzzle(fm.getMatrix()))
        except:
            print("File tidak ditemukan")
            exit()
    else:
        print("Input salah")
        exit()

    '''
    Tahap Inisiasi
    '''
    # menginisiasi root
    root.root.printBoard()
    print()

    # mengecek apakah puzzle dapat diselesaikan
    if(not root.root.solveable()):
        print("Puzzle tidak dapat diselesaikan.")
        exit()

    print("Puzzle dapat diselesaikan.")
    print()

    # menginisiasi simpul yang dibuat
    nodeCount = 1

    # cost terendah diprioritaskan dalam priority queue
    costFunction = numberMisplacedTiles
    pq = PriorityQueue(lambda x,y : x.depth + costFunction(x.root) <= y.depth + costFunction(y.root))

    # menginisiasi priority queue
    pq.push(root)

    # variabel menyimpan state solusi
    solutionState = None

    # variabel menyimpan kemungkinan move di puzzle
    movesUnits = [(-1,0), (0,-1), (1,0), (0,1)]
    movesNames = ["Up", "Left", "Down", "Right"]

    # Start timer
    time_start = time.process_time_ns()
    

    '''
    Tahap Pencarian Dengan Branch and Bound
    '''
    while(not pq.isEmpty()):
        # mengambil item palign depan dari queue
        current = pq.front()
        pq.pop()

        # jika puzzle sudah terurut maka simpan state lalu berhenti
        if(isFinish(current.root)):
            solutionState = current
            break

        # memasukkan setiap status yang mungkin ke priority queue
        for i, (dr, dc) in enumerate(movesUnits):
            if(movesNames[(i+2)%4] != current.move):
                # membuat simpul
                result = Node(current.root.move(dr, dc), parent=current, depth=current.depth+1, move=movesNames[i])

                # Jika move bisa dilakukan, maka tambahkan ke priority queue
                if(result != None and result.root != None):
                    nodeCount += 1
                    pq.push( result )

    # Stop timer
    time_end = time.process_time_ns()

    '''
    Tahap Output
    '''
    # membuat array yang berisi simpul simpul dari pohon ruang status yuang diambil
    solutionArray = generateSolution(solutionState)

    # Total moves yang dilakukan
    print("Total moves:", len(solutionArray))

    # Banyak simpul dibuat
    print(nodeCount,"simpul dibuat")

    # Total waktu yang digunakan
    total_time = time_end - time_start
    print("Total waktu: ", total_time / 1000000, "ms")

if __name__ == "__main__":
    main()
