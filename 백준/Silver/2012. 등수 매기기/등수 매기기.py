import sys
input = sys.stdin.readline

N = int(input())
rank = [0] + sorted([int(input()) for _ in range(N)])

bad = 0
for i in range(1, N + 1):
	bad += abs(i - rank[i])
print(bad)