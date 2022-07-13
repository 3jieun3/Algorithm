import sys
input = sys.stdin.readline

N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))

rst = [0] * M
for i in range(M):
	target = targets[i]         # 찾을 숫자
	li, ri = 0, N - 1           # 인덱스 초기화
	while li <= ri:
		mi = (li + ri) // 2     # mid 인덱스
		card = cards[mi]

		if target == card:      # 찾은 경우
			rst[i] = 1
			break

		if target > card:       # 더 큰 경우 오른쪽으로(큰쪽)
			li = mi + 1
		else:                   # 더 작은 경우 왼쪽으로(작은쪽)
			ri = mi - 1

print(*rst)