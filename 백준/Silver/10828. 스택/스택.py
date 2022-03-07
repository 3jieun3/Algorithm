import sys
input = sys.stdin.readline
class stack:
    def __init__(self):
        self.st = []
    
    def size(self):
        print(len(self.st))
    
    def push(self, x):
        self.st.append(x)
    
    def pop(self):
        if len(self.st) == 0:
            print('-1')
        else:
            print(self.st.pop(-1))
    
    def empty(self):
        if len(self.st) == 0:
            print('1')
        else:
            print('0')
            
    def top(self):
        if len(self.st) == 0:
            print('-1')
        else:
            print(self.st[-1])
            
stck = stack()
n = int(input())
for _ in range(n):
    inst = input()
    if 'push' in inst:
        stck.push(inst.split()[1])
    elif 'pop' in inst:
        stck.pop()
    elif 'size' in inst:
        stck.size()
    elif 'top' in inst:
        stck.top()
    elif 'empty' in inst:
        stck.empty()