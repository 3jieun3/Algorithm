import sys
input = sys.stdin.readline

N = int(input())
pos = sorted(list(map(int, input().split())))
mid = N // 2    # 중간 인덱스
if N % 2:       # 홀수개인 경우
	print(pos[mid])
else:           # 짝수개인 경우
	sum_l, sum_r = 0, 0
	for i in range(N):
		sum_l += abs(pos[i] - pos[mid - 1])
		sum_r += abs(pos[i] - pos[mid])
	if sum_l <= sum_r:
		print(pos[mid - 1])
	else:
		print(pos[mid])