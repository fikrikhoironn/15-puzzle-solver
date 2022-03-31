class PriorityQueue:
    def __init__(self, prio_func):
        self.queue = []
        self.func = prio_func

    def is_empty(self):
        return len(self.queue) == 0
    
    def front(self):
        return self.queue[0]

    def enqueue(self, item):
        pos = 0
        found = False
        while(pos < len(self.queue) and not found):
            if self.func(item, self.queue[pos]):
                found = True
            else:
                pos += 1
        
        self.queue.insert(pos, item)
    
    def dequeue(self):
        self.queue.pop(0)
