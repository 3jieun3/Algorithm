import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))
M = int(input())    # 총 예산

if sum(arr) <= M:   # 1. 모든 요청이 배정될 수 있는 경우
	print(arr[-1])      # 최대 금액 출력
else:               # 2. 없는 경우
	l, r = 1, M
	while l <= r:
		mid = (l + r) // 2
		ssum = 0
		for x in arr:
			if x <= mid:
				ssum += x
			else:
				ssum += mid
		if ssum > M:			# 예산 넘으면 상한선 더 작게
			r = mid - 1
		else:					# 예산 안 넘으면 상한선 더 크게
			l = mid + 1
	print(r)