import sys
input = sys.stdin.readline

T = int(input())
result = [0] * T
for tc in range(T):
	N = int(input())                            # 날 수
	array = list(map(int, input().split()))     # 날 별 주가
	profit = 0                                  # 이익
	# 마지막날부터 피크 주가인 날 탐색 -> 더 큰 주가 나오기전까지 차액으로 이익증가
	mx_val = array[-1]          # 피크 주가 초기화
	for i in range(N - 2, -1, -1):
		if array[i] > mx_val:   # 더 큰 주가 - 피크 주가 갱신
			mx_val = array[i]
		elif array[i] < mx_val: # 작은 주가 - 차액으로 이익 증가
			profit += (mx_val - array[i])
		else:                   # 같은 주가 - 아무것도 안함
			pass

	result[tc] = profit

for tc in range(T):
	print(result[tc])