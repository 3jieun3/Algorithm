#1  2  3  4 '5' 6 7 8 9  -> 1 + 2 + 3 + 4 = 10 < 14  | (1 5 9) -> (1 5 4)
#1 '2' 3  4              -> 4 + 5 + 9 + 10 = 28 > 14 | (1 2 4) -> (3 2 4)
#     '3' 4              -> 3 + 3 + 6 + 6 = 18 > 14  | (3 3 4) -> (4 3 4)
#        '4'             -> 2 + 2 + 4 + 5 = 13 < 14  | (4 4 4) -> (4 4 3)

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
have = [int(input()) for _ in range(K)]
mx_rst = 0          # 만들 수 있는 최대 랜선 길이

left = 1            # 랜선 길이 범위
right = max(have)   # 랜선 길이 범위
while left <= right:
	cnt = 0
	mid = (left + right) // 2   # 가운데 값 길이로 만든다면
	for i in range(K):
		cnt += have[i] // mid

	if cnt >= N:                # N개 이상 만들어지면 더 크게 자르기
		left = mid + 1
	else:                       # N개 안만들어지면 더 작게 자르기
		right = mid - 1
print(right)