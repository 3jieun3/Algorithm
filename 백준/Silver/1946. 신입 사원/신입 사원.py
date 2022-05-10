import sys
input = sys.stdin.readline

T = int(input())
results = [0] * T
for tc in range(T):
	N = int(input())
	ranks = sorted([list(map(int, input().split())) for _ in range(N)])     # 서류(높은 순위 기준), 면접
	newbies = 1
	a, b, = ranks[0]
	for i in range(1, N):
		if b > ranks[i][1]:
			b = ranks[i][1]
			newbies += 1
	results[tc] = newbies
for tc in range(T):
	print(results[tc])