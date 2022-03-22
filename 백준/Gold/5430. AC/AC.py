import re
import sys
from collections import deque
input = sys.stdin.readline
ch = re.compile("[0-9]+")

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    x = input()[1:-2].split(',')
    arr = deque()
    for i in range(n):
        arr.append(x[i])

    reverseFlag = False
    errorFlag = False
    
    for inst in p:
        if inst == 'R':
            # reverse() 는 시간초과 발생하므로 플래그 사용
            if reverseFlag == False: reverseFlag = True
            else: reverseFlag = False

        elif inst == 'D':
            if len(arr) == 0:
                errorFlag = True
                break
            else:
                if reverseFlag == False:
                    arr.popleft()
                else:
                    arr.pop()
    
    if errorFlag == True:
        print("error")
    elif reverseFlag == True:
        arr.reverse()
        print('['+','.join(list(arr))+']')
    else:
        print('['+','.join(list(arr))+']')