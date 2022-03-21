# list 의 연산은 O(1) , deque의 연산은 O(1)
from collections import deque
deq = deque()
n = int(input())
for i in range(1, n+1):
    deq.append(i)

for _ in range(n-1):
    deq.popleft()
    deq.rotate(-1)

print(deq.pop())