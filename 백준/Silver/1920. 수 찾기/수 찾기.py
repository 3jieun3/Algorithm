# set 의 탐색은 O(1)
# list 의 탐색은  O(n)

import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

rst = [0] * M
for i in range(M):
	x = targets[i]
	if x in A:
		rst[i] = 1

print(*rst, sep="\n")
