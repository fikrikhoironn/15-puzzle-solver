import heapq
class PriorityQueue:
    '''
    membuat priorityFunction
    '''
    def __init__(self, priorityFunction):
        self.queue = []
        self.function = priorityFunction
    
    '''
    memasukkan elemen ke antrian sesuai dengan fungsi yang didefinisikan
    '''
    def push(self, item):
        pos = 0
        found = False

        while(not found and pos < len(self.queue)):
            if(self.function(item, self.queue[pos])):
                found = True
            else:
                pos+=1
        
        self.queue.insert(pos, item)

    '''
    melakukan pop elemen dari antrian
    '''
    def pop(self):
        self.queue.pop(0)

    '''
    melihat elemen antrian terdepan
    '''
    def front(self):
        return self.queue[0]

    '''
    mengecek apakah priority queue kosong
    '''
    def isEmpty(self):
        return len(self.queue) == 0

