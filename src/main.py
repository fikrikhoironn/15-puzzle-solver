# main.py
# Contains main program and several functions for aiding Branch and Bound

from Puzzle import Puzzle
from FileManager import FileManager
from PriorityQueue import PriorityQueue
from Tree import Tree
from Constant import SIZE
from PuzzleGenerator import PuzzleGenerator
import time

# g(i) function for checking misplaced tiles
def number_misplaced_tiles(puzzle):
    result = 0
    flat = puzzle.flattened_board()
    
    for i in range(1, SIZE**2+1):
        if(flat[i-1] != i):
            result+=1

    return result

# Check whether matrix is sorted or not
def is_finish(puzzle):
    flat = puzzle.flattened_board()
    for i in range(1, (SIZE**2)+1):
        if(flat[i-1] != i):
            return False

    return True

# Generate solution from solved node
def generate_solution(solved_state):
    tree_solution = []

    parent = solved_state.parent
    state = solved_state

    while(parent != None):
       tree_solution.insert(0, state) 
       state = parent
       parent = parent.parent
    for i in range(len(tree_solution)):
        tree_solution[i].root.output_board()
    return tree_solution


def main():
    choose = int(input("1. Random puzzle\n2. Input puzzle\n"))
    if (choose == 1):
        file = PuzzleGenerator()
        root = Tree(Puzzle(file.get_board()))
    elif(choose == 2):
        filename = input("Masukkan nama file puzzle: ")
        try:
            fm = FileManager("../test/" + filename)
            root = Tree(Puzzle(fm.get_board()))
        except:
            print("File tidak ditemukan")
            exit()
    else:
        print("Input salah")
        exit()
    # Initiate root
    root.root.output_board()
    print()
    # Check if puzzle is solveable
    if(not root.root.is_solveable()):
        print("Puzzle tidak dapat diselesaikan.")
        exit()

    print("Puzzle dapat diselesaikan.")
    print()

    # Node generated count
    node_count = 1

    # Make priority queue for branching
    # On priority : lowest cost with last in first
    cost_function = number_misplaced_tiles


    pq = PriorityQueue(lambda x,y : x.depth + cost_function(x.root) <= y.depth + cost_function(y.root))

    # Initiate priority queue
    pq.push(root)

    # Variable to store solution state
    solution_state = None

    # List possible moves for puzzle
    moves_units = [(-1,0), (0,-1), (1,0), (0,1)]
    moves_names = ["Up", "Left", "Down", "Right"]

    # Start timer
    time_start = time.process_time_ns()

    # Searching for solution using Branch and Bound

    while(not pq.is_empty()):
        # Get front item in queue
        current = pq.front()
        pq.pop()

        # If currently checking final state, save the current state
        if(is_finish(current.root)):
            solution_state = current
            break

        # Append generate states to pq
        for i, (dr, dc) in enumerate(moves_units):
            # If moves are NOT opposite to previous move, generate new node
            if(moves_names[(i+2)%4] != current.move):
                # Generate node
                result = Tree(current.root.move(dr, dc), parent=current, depth=current.depth+1, move=moves_names[i])

                # If move is possible..
                if(result != None and result.root != None):
                    node_count += 1
                    pq.push( result )

    # Stop timer
    time_stop = time.process_time_ns()

     # Generate solution from result
    solution_array = generate_solution(solution_state)
    # Output details
    print("Total moves:", len(solution_array))

    # Output nodes generated
    print(node_count,"simpul dibuat")

    # Output time
    time_delta = time_stop - time_start
    print("Total waktu: ", time_delta / 1000000, "ms")

if __name__ == "__main__":
    main()
