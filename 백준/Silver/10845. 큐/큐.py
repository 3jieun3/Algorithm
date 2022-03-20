import sys
input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.q = []
    
    def size(self):
        print(len(self.q))
    
    def push(self, x):
        self.q.append(x)
    
    def pop(self):
        if len(self.q) == 0:
            print('-1')
        else:
            print(self.q.pop(0))
    
    def empty(self):
        if len(self.q) == 0:
            print('1')
        else:
            print('0')
            
    def front(self):
        if len(self.q) == 0:
            print('-1')
        else:
            print(self.q[0])
    
    def back(self):
        if len(self.q) == 0:
            print('-1')
        else:
            print(self.q[-1])
            
queue = Queue()
n = int(input())
for _ in range(n):
    inst = input()
    
    if 'push' in inst:
        queue.push(inst.split()[1])
        
    elif 'pop' in inst:
        queue.pop()
            
    elif 'size' in inst:
        queue.size()
        
    elif 'front' in inst:
        queue.front()
    
    elif 'back' in inst:
        queue.back()
        
    else:
        queue.empty()