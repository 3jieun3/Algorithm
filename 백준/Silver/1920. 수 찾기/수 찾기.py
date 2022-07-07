import sys
n = int(input())
a = set(map(int, sys.stdin.readline().split()))
# set 의 탐색은 O(1)
# list 의 탐색은  O(n)
m = int(input())
target = list(map(int, sys.stdin.readline().split()))

for x in target:
    if x in a: print('1')
    else: print('0')
    